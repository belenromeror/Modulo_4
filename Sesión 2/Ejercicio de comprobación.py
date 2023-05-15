#Diseño de una clase
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso

# Instancias
caballo = Animal(nombre="Zeus", edad="5 años", raza="Pura Sangre", peso="450 kg")
león = Animal(nombre="Boulder", edad="10 años", raza="Atlas", peso="130 kg")

