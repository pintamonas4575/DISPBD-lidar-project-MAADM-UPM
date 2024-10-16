
"""
Archivo que junta todas las imágenes de los frames y crea un GIF, mostrando la animación correspondiente
a la transición de los vehículos por el pórtico
"""

from PIL import Image
import os

carpeta = "cluster_images"
nombre_gif = 'prueba66_limpio.gif'

def ordenar_cifras_png(archivo: str):
    partes = archivo.split('_')
    primera_cifra = int(partes[0])
    segunda_cifra = int(partes[1].split('.')[0])  
    return (primera_cifra, segunda_cifra)

archivos = [archivo for archivo in os.listdir(carpeta)]
archivos_ordenados = sorted(archivos, key=ordenar_cifras_png)

frames = [Image.open(f'{carpeta}/{imagen}') for imagen in archivos_ordenados]

frames[0].save(nombre_gif,
               format='GIF', 
               append_images=frames[1:], 
               save_all=True, 
               duration=50, 
               loop=0)  
