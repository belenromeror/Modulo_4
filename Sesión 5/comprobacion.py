class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")

#Definición de la clase C con herencia multiple de B y A

class C(B, A):
    def metodo_c(self):
        print("Metodo de clase C")

#Creación de instancia

c = C()
c.metodo_a()
c.metodo_b()
c.metodo_c()

