# Documentación para `carpetas.py`

## Descripción

Este script automatiza la creación de una carpeta con un nombre único basado en la fecha y hora actuales. Dentro de esta carpeta, genera 10 archivos de texto, cada uno con la fecha y hora de creación escrita en su contenido. Si la carpeta ya existe, la elimina antes de crear una nueva. Es útil para tareas como pruebas, generación de datos o almacenamiento organizado.

## Uso

```bash
python carpetas.py
```
## Autor

Laura Juliana Picón Acosta

## Instalación

 generar_readme_programa.py: Crear un readme para un programa especifico
 hello.py: ejercicio de clase
 prueba.sh: ejercicio de clase

 carpetas.py: Crear carpetas en un directorio usando nombres aleatorios

 1. Importación de módulos
os: Proporciona funciones para interactuar con el sistema operativo, como crear carpetas y manejar rutas de archivos.
shutil: Permite realizar operaciones de alto nivel con archivos y directorios, como eliminar carpetas completas.
datetime: Se utiliza para trabajar con fechas y horas, en este caso, para generar nombres dinámicos y registrar la fecha y hora de creación.
2. Definición de la función principal
Esta función encapsula toda la lógica para crear una carpeta y generar los archivos dentro de ella.
3. Generación de un nombre dinámico para la carpeta
datetime.now(): Obtiene la fecha y hora actual.
strftime('%Y%m%d_%H%M%S'): Formatea la fecha y hora en un formato legible (por ejemplo, 20250429_153045).
f"carpeta_{...}": Crea un nombre único para la carpeta basado en la fecha y hora.
4. Verificación y eliminación de la carpeta existente
os.path.exists(nombre_carpeta): Verifica si la carpeta ya existe.
shutil.rmtree(nombre_carpeta): Si la carpeta existe, la elimina junto con todo su contenido.
5. Creación de la nueva carpeta
os.makedirs(nombre_carpeta): Crea la carpeta con el nombre generado dinámicamente.
6. Creación de 10 archivos dentro de la carpeta
for i in range(1, 11): Itera del 1 al 10 para crear 10 archivos.
f"archivo_{i}.txt": Genera nombres de archivo dinámicos como archivo_1.txt, archivo_2.txt, etc.
os.path.join(nombre_carpeta, nombre_archivo): Combina la ruta de la carpeta con el nombre del archivo para obtener la ruta completa.
7. Escribir la fecha y hora de creación en cada archivo
open(ruta_archivo, "w"): Abre el archivo en modo escritura. Si no existe, lo crea.
archivo.write(...): Escribe la fecha y hora actual dentro del archivo.
with: Asegura que el archivo se cierre automáticamente después de escribir.
8. Mensaje de confirmación
Muestra un mensaje en la consola indicando que la carpeta y los archivos se han creado correctamente.
9. Ejecución del script
if __name__ == "__main__":: Asegura que la función crear_carpeta_y_archivos solo se ejecute si el script se ejecuta directamente, no si se importa como módulo.

*Generado automáticamente desde docstring*