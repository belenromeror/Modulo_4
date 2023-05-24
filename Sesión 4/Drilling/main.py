from persona import Persona
from ciclista import Ciclista
from maratonista import Maratonista

persona_1 = Persona('Onofrio')
persona_1.movimiento('Caminando')
print(persona_1.nombre)

ciclista = Ciclista('Raul')
ciclista.movimiento('rodando')

maratonista = Maratonista('Ezio')
maratonista.movimiento('trotando')

