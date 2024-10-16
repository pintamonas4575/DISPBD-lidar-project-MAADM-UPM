
"""
Bucle que se repite a lo largo de todos los frames limpiados de clústers
inválidos para descargar la imagen correspondiente a cada frame
"""

import os
import numpy as np
import pandas as pd
import pyvista as pv
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
# ---------------------------------------------------------------
# Función ordenar por nombre
def ordenar_cifras(archivo: str):
    partes = archivo.split('_')
    primera_cifra = int(partes[1])
    segunda_cifra = int(partes[2].split('.')[0])  
    return (primera_cifra, segunda_cifra)

carpeta_origen = "pointclouds_limpio"

archivos = [archivo for archivo in os.listdir(carpeta_origen)]
archivos_ordenados = sorted(archivos, key=ordenar_cifras)
# ---------------------------------------------------------------

CAMERA_POSITION = None
carpeta_destino = 'cluster_images'
offset = 0

for indice, archivo in enumerate(archivos_ordenados): 

    frame_id = archivo.split('pointcloud_')[1].split('.csv')[0]

    csv = pd.read_csv(f'{carpeta_origen}/{archivo}')
    data_frame = pd.DataFrame(csv)

    X = data_frame['x']
    Y = data_frame['y']
    Z = data_frame['z']

    points = np.column_stack((Y, X, Z))  # combinación buena
    scaler = StandardScaler()
    points_scaled = scaler.fit_transform(points)

    db = DBSCAN(eps=0.6, min_samples=25).fit(points_scaled)
    labels = db.labels_

    plotter = pv.Plotter(window_size=[800, 500])
    plotter.set_background('black')
    cloud = pv.PolyData(points)
    plotter.add_mesh(cloud, render_points_as_spheres=True, point_size=5, color='lime', show_scalar_bar=False)

    unique_labels = np.unique(labels[labels != -1])  # Excluir ruido

    bounding_boxes = []
    centroides = []

    for label in unique_labels:
        cluster_points = points[labels == label]

        centroide = np.mean(cluster_points, axis=0)
        centroides.append(centroide)

        min_x, min_y, min_z = np.min(cluster_points, axis=0)
        max_x, max_y, max_z = np.max(cluster_points, axis=0)
        
        bounding_boxes.append((min_x, max_x, min_y, max_y, min_z, max_z))

    for bbox in bounding_boxes:
        min_x, max_x, min_y, max_y, min_z, max_z = bbox
        box = pv.Cube(bounds=(min_x, max_x, min_y, max_y, min_z, max_z))
        plotter.add_mesh(box, color='red', style='wireframe', line_width=1.5)

    for i, centroide in enumerate(centroides):
        centroide[2] += 2 # mover etiqueta más arriba
        plotter.add_point_labels(centroide, [f"Cluster {i}"], point_size=10, font_size=20, text_color="#00FFFF")

    plotter.show_axes()

    plotter.camera.zoom(1.3)
    if indice == 0:
        CAMERA_POSITION = plotter.camera_position  
    else:
        plotter.camera_position = CAMERA_POSITION

    plotter.off_screen = True
    plotter.screenshot(f'{carpeta_destino}/{frame_id}_{indice+offset}.png', window_size=[1920, 1080])
    plotter.close()
