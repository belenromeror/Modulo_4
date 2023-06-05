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
        
   