import ast
import sys
from pathlib import Path

def extraer_docstring(archivo_py):
    with open(archivo_py, "r", encoding="utf-8") as f:
        nodo = ast.parse(f.read())
        return ast.get_docstring(nodo)

def generar_readme(nombre_archivo):
    archivo = Path(nombre_archivo)
    docstring = extraer_docstring(archivo)
    
    if not docstring:
        print(f"No se encontró docstring en {archivo.name}")
        docstring = "Descripción pendiente..."

    contenido = f"# Documentación para `{archivo.name}`\n\n"
    contenido += f"## Descripción\n\n{docstring}\n\n"
    contenido += f"## Uso\n\n```bash\npython {archivo.name}\n```\n"
    contenido += f"## Autor\n\n*Generado automáticamente desde docstring*\n"

    nombre_readme = f"README_{archivo.stem}.md"
    with open(nombre_readme, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"✅ README generado: {nombre_readme}")

# -----------------------------
# Ejecución
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python generar_readme_desde_docstring.py archivo.py")
    else:
        generar_readme(sys.argv[1])

