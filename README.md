# Lidar-project-MAADM-UPM

Proyecto de clusterización que utiliza un conjunto de CSVs de un pórtico con lídar (INSIA) y clusteriza los vehículos en cada frame. Perteneciente a la asgnatura **Diseño de sistemas de adquisición y procesamiento masivo de datos** del **Máster Universitario En Aprendizaje Automático y Datos Masivos (MAADM)** de la **UPM**. 

Se basa en el algortimo DBSCAN (**D**ensity-**B**ased **S**patial **C**lustering of **A**pplications with **N**oise) para averiguar el número de clústers en una nube de puntos.

# 📓 Notebooks *1, 2 y 3 .ipynb*

Notebooks que muestran el proceso de clusterizar y etiquetar una nube de puntos con vehículos.

- *1_archivos_coches.ipynb*: Clustering de situaciones más simples. Trabaja con los CSVs que empiezan por 'C_...' en la carpeta "data".
- *2_limpiar_clusters.ipynb*: Ejemplo de eliminación de clústers "inválidos" en un frame.
- *3_video_frames.ipynb*: Proceso entero hasta clusterizar y etiquetar un frame. 

# 📓 Archivo *prueba5_frames.py*

Notebook que analiza cada frame (CSV), clusteriza, etiqueta y guarda una imagen de la situación.

# 📓 Archivo *gif.py*

Convierte todas las imágenes generadas por el archivo "prueba5_frames" en GIF para poder apreciar el paso del tiempo como un vídeo.

☣️☣️ 
**NOTA:** Ajustar los paths para el correcto funcionamiento de los archivos.
☣️☣️

# 📂 Carpeta *"data"*

En ella se encuentran los CSVs de prueba ya manipulados para su utilización directa en los notebooks.

# 📂 Carpeta *"results"*

En ella se muestran los resultados del clustering a lo largo de los frames.

# ⚖️ Licencia 

El gobierno no sabe clusterizar bien sus ideas, así nos va.

# 👤 Contacto

Cualquier duda o sugerencia contactar con el autor:

Alejandro Mendoza: alejandro.embi@gmail.com