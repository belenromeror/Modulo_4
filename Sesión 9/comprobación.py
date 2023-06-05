def agregar_info_al_archivo(texto):
    try:
        with open ("informacion.dat", "a", encoding="utf-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: ARCHIVO NO ENCONTRADO")
    except Exception as e:
        print("ERROR: ", e)
agregar_info_al_archivo("Hola Mundo")
agregar_info_al_archivo("Este en una nueva línea en el archivo")
agregar_info_al_archivo("agregando la segunda línea del archivo")
agregar_info_al_archivo("finalizando la línea agregada")


def reemplazar_datos_archivos(texto_viejo, texto_nuevo):
    numero= 0
    try:
        archivo = open("informacion.dat", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        reemplazo=""
        for linea in lineas:
            if texto_viejo in linea:
                linea = linea.replace(texto_viejo, texto_nuevo)
                reemplazo +=linea
                numero +=1
        if numero>0:
            archivo_reemplazo =open("informacion.dat", "w", encoding ="utf-8")
            archivo_reemplazo.write(reemplazo)   
            archivo_reemplazo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    except Exception as error:
        print('Se ha generado un error no previsto',
        type(error).__name__)
    finally:
        print("se realizaron", numero, "reemplazos")
reemplazar_datos_archivos("información", "Procesamiento")





