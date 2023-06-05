from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self,marca, modelo, numero_ruedas, velocidad, cilindrada ):
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

        