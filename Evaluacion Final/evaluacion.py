class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
            
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
        
    @property
    def numero_ruedas(self):
        return self._numero_ruedas
    
    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas):
        self._numero_ruedas = numero_ruedas
    
class Automovil(Vehiculo):
    def __init__(self,marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    @property
    def velocidad(self):
        return self.velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    @property
    def cilindrada(self):
        return self._cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

class Automovilservice():        

    def crear_automovil (self, contador):
        marca = input ("Ingrese marca del automovil: ")
        modelo = input ("Ingrese modelo del automovil: ")
        numero_ruedas = input ("Ingrese el número de ruedas: ")
        cilindrada = input ("Ingrese la cilindrada del automovil: ")
        velocidad = input ("Ingrese la velocidad del automovil: ")
        automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
        print (f"Vehiculo{contador} creado: ", automovil)
        lista.append(automovil)
    

ingreso = int(input("¿Cuantos automoviles desea ingresar?"))
lista = []
i=1
automovil_service = Automovilservice()

while i<= ingreso:
    automovil_service.crear_automovil(i)
    i+=1

print("La lista de automoviles creados es:", lista)


    