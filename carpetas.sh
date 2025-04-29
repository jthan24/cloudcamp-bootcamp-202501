#!/bin/bash

# Generar un nombre único para la carpeta basado en la fecha y hora actuales
nombre_carpeta="carpeta_$(date +%Y%m%d_%H%M%S)"

# Si la carpeta ya existe, eliminarla
if [ -d "$nombre_carpeta" ]; then
  rm -rf "$nombre_carpeta"
fi

# Crear la carpeta
mkdir "$nombre_carpeta"

# Crear 10 archivos dentro de la carpeta
for i in {1..10}; do
  nombre_archivo="archivo_$i.txt"
  ruta_archivo="$nombre_carpeta/$nombre_archivo"
  
  # Escribir la fecha y hora de creación en cada archivo
  echo "Fecha y hora de creación: $(date)" > "$ruta_archivo"
done

echo "Carpeta '$nombre_carpeta' creada con 10 archivos."