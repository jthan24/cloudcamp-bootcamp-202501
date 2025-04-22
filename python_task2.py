import os
import datetime

def crear_carpetas_mensuales():
    """
    Crea una carpeta con el año actual y dentro subcarpetas para los 10 meses a partir de enero.
    """
    año_actual = datetime.datetime.now().year
    nombre_carpeta_año = str(año_actual)

    try:
        # Crear la carpeta del año si no existe
        if not os.path.exists(nombre_carpeta_año):
            os.makedirs(nombre_carpeta_año)
            print(f"Carpeta '{nombre_carpeta_año}' creada exitosamente.")
        else:
            print(f"La carpeta '{nombre_carpeta_año}' ya existe.")

        # Crear las carpetas de los 10 meses
        #meses = ["01_Enero", "02_Febrero", "03_Marzo", "04_Abril", "05_Mayo",
        #         "06_Junio", "07_Julio", "08_Agosto", "09_Septiembre", "10_Octubre"]

        for mes in range (1,11):
            ruta_carpeta_mes = os.path.join(nombre_carpeta_año, str(mes))
            if not os.path.exists(ruta_carpeta_mes):
                os.makedirs(ruta_carpeta_mes)
                print(f"Carpeta ' {mes} 'creada en '{nombre_carpeta_año}'.")
            else:
                print(f"La carpeta ' {mes}' ya existe en '{nombre_carpeta_año}'.")

        print("Proceso completado.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    crear_carpetas_mensuales()