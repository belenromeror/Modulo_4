from service import Automovilservice
from automovil import Automovil
from vehiculo import Vehiculo

ingreso = int(input("¿Cuantos automoviles desea ingresar?"))
i=1
automovil_service = Automovilservice()

while i<= ingreso:
    automovil_service.crear_automovil(i)
    i+=1

automovil = Automovil(marca,modelo,numero_ruedas,velocidad, cilindrada)

    