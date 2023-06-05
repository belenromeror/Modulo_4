from automovil import Automovil
from vehiculo import Vehiculo

class Automovilservice(Automovil, Vehiculo):        

    def crear_automovil (self, contador):
        marca = input ("Ingrese marca del automovil: ")
        modelo = input ("Ingrese modelo del automovil: ")
        numero_ruedas = input ("Ingrese el número de ruedas: ")
        cilindrada = input ("Ingrese la cilindrada del automovil: ")
        velocidad = input ("Ingrese la velocidad del automovil: ")
        automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
        print (f"Vehiculo{contador} creado: ", automovil)
