#Diseño de una clase
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
#Se definen los metodos 
    def comer(self):
        print(f"{self.nombre} está comiendo")
    
    def caminar(self):
        print(f"{self.nombre} está caminando")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Instancias
perro = Animal(nombre="Brando", raza="San Bernardo", edad=3, peso=30)
gato = Animal(nombre="Roll", raza="Persa", edad=4, peso=3)


