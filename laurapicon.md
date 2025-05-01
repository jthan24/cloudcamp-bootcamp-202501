Laura_picon: README

1. Crear Fork del proyecto original: https://github.com/jthan24/cloudcamp-bootcamp-202501/fork
2. Clonar el proyecto cloudcamp-bootcamp-202501: git clone https://github.com/julianapicon/cloudcamp-bootcamp-202501.git
3. Crear rama feature: $ git checkout -b feature/laurap
4. Crear archivo laurapicon.md: $ touch laurapicon.md
5. Generar contenido README: $ echo "Contenido" > laurapicon.md
6. Guardar cambios en local
7. Adicionar cambios a stage: $ git add .
8. Generar commit: $ git commit -m "este es mi primer commit del cloudcamp DevOps"
9. Subo los cambios de la feature al remoto: $ git push origin feature/laurap
10. Ingreso al proyecto en GitHub para crear el pull request, desde feature/laurap hacia la rama principal
10. Mezclar el contenido con el repositorio original:
    $ git checkout main
    $ git pull
    $ git merge feature/laurap
    $ git push origin main  