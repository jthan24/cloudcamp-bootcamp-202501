"""
Este script automatiza la creación de una carpeta con un nombre único basado en la fecha y hora actuales. Dentro de esta carpeta, genera 10 archivos de texto, cada uno con la fecha y hora de creación escrita en su contenido. Si la carpeta ya existe, la elimina antes de crear una nueva. Es útil para tareas como pruebas, generación de datos o almacenamiento organizado.
"""

import os
import shutil
from datetime import datetime

def crear_carpeta_y_archivos():
    # Crear un nombre dinámico para la carpeta basado en la fecha y hora actual
    nombre_carpeta = f"carpeta_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Si la carpeta ya existe, eliminarla
    if os.path.exists(nombre_carpeta):
        shutil.rmtree(nombre_carpeta)
    
    # Crear la carpeta
    os.makedirs(nombre_carpeta)
    
    # Crear 10 archivos dentro de la carpeta
    for i in range(1, 11):
        nombre_archivo = f"archivo_{i}.txt"
        ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)
        
        # Escribir la fecha y hora de creación en cada archivo
        with open(ruta_archivo, "w") as archivo:
            archivo.write(f"Fecha y hora de creación: {datetime.now()}\n")
    
    print(f"Carpeta '{nombre_carpeta}' creada con 10 archivos.")

if __name__ == "__main__":
    crear_carpeta_y_archivos()