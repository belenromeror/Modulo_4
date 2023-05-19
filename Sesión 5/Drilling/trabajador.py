
from departamento import Departamento
from persona import Persona

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto) -> None:
        Persona.__init__(self,nombre,apellido,anno)
        Departamento.__init__(self,nombre_dpto,nombre_corto_dpto)
        self.salario = 0
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario