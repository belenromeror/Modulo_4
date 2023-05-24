def crear_archivo():
    try:
        file = open("informacion.dat", "x")  # Usar "x" en lugar de "w" para evitar sobrescribir el archivo existente
        file.close()  # Cerrar el archivo
    except FileExistsError:
        print("Error: El archivo ya existe")
    except Exception as e:  # Otros errores
        print(f"Error: {e}")

def escribir_archivo(lista):
    try:
        with open("informacion.dat", "w") as file:
            for dato in lista:
                file.write(dato)
    except Exception as e:
        print(f"Error: {e}")

def leer_archivo():
    try:
        with open("informacion.dat", "r") as file:
            datos = file.readlines()
            for linea in datos:
                print(linea.strip())
    except FileNotFoundError:
        print("Error: El archivo no existe")
    except Exception as e:
        print(f"Error: {e}")

lista = ["Datos de información en la línea 1", "\nDatos de información en la línea 2", "\nDatos de información en la línea 3", "\nDatos de información en la línea 4", "\nDatos de información en la línea 5"]

crear_archivo()
escribir_archivo(lista)
leer_archivo()