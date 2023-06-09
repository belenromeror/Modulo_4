#Diseño de una clase
class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self. estatura = estatura
        self.peso = peso
#Definición de funciones get y set    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_apellidos(self):
        return self.apellidos
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
        
    def get_sexo(self):
        return self.sexo
    
    def set_sexo(self, sexo):
        self.sexo = sexo
        
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad
        
    def get_estatura(self):
        return self.estatura
    
    def set_estatura(self, estatura):
        self.estatura = estatura
        
    def get_peso(self):
        return self.peso
    
    def set_peso(self, peso):
        self.peso = peso

# Crear los objetos de la clase Persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

# Modificar los atributos solicitados
persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")

# Imprimir los atributos actualizados
print("Persona_1:")
print("Nombre:", persona_1.get_nombre())
print("Apellidos:", persona_1.get_apellidos())
print("Sexo:", persona_1.get_sexo())
print("Edad:", persona_1.get_edad())
print("Estatura:", persona_1.get_estatura())
print("Peso:", persona_1.get_peso())

print("Persona_2:")
print("Nombre:", persona_2.get_nombre())
print("Apellidos:", persona_2.get_apellidos())
print("Sexo:", persona_2.get_sexo())
print("Edad:", persona_2.get_edad())
print("Estatura:", persona_2.get_estatura())
print("Peso:", persona_2.get_peso())

