# Documentación para `carpetas.sh`

## Descripción

Este script automatiza la creación de una carpeta con un nombre único basado en la fecha y hora actuales. Dentro de esta carpeta, genera 10 archivos de texto, cada uno con la fecha y hora de creación escrita en su contenido. Si la carpeta ya existe, la elimina antes de crear una nueva. Es útil para tareas como pruebas, generación de datos o almacenamiento organizado.

## Uso

```bash
```
## Autor

Laura Juliana Picón Acosta

## Instalación

nombre_carpeta="carpeta_$(date +%Y%m%d_%H%M%S)": Genera un nombre único para la carpeta usando la fecha y hora actuales.

if [ -d "$nombre_carpeta" ]; then rm -rf "$nombre_carpeta"; fi: Verifica si la carpeta ya existe y, si es así, la elimina.

mkdir "$nombre_carpeta": Crea la carpeta con el nombre generado.

for i in {1..10}: Itera del 1 al 10 para crear 10 archivos.

echo "Fecha y hora de creación: $(date)" > "$ruta_archivo": Escribe la fecha y hora actuales en cada archivo.

chmod +x crear_carpeta.sh: Hace que el script sea ejecutable.