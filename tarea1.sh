#/!bin/bash 
#indica que debe interpretarse con bash
#Creacion de una carpeta con nombre dinamico con fecha y hora
folder_name="carpeta_$(date +%Y%m%d_%H%M%S)"
#Condicion si exite la carpeta eliminarla
if [ -d "folder_name" ]; then
  rm -r "folder_name"
fi
#Creacion de carpeta
mkdir "$folder_name"
#Creacion de archivos dentro de la carpeta
for i in {1..10}; do
    file_path="$folder_name/archivo_$i.txt"
    echo "archivo creado el : $(date)" > "$file_path"
done
