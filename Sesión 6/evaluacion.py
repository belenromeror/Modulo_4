usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = "004"

#Se realiza el manejo de excepciones para el dato que no se encuentra definido en el diccionario.
try:
    print(usuarios[id_usuario])
except KeyError:
    print(f"La clave {id_usuario} no está en el diccionario. Añadiendo clave...")
    usuarios[id_usuario] = None

#Imprime el nuevo diccionario
print(usuarios)