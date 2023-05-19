#Diseño de las clases solicitadas
class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def anno(self):
        return self._anno
    
    @anno.setter
    def anno(self, anno):
        self._anno = anno