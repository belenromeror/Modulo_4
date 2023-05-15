class Banco:
    def __init__(self, nombre, codigo, direccion):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.clientes = []
        self.cuentas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def transferencia(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen.saldo >= monto:
            cuenta_origen.retirar(monto)
            cuenta_destino.depositar(monto)
            print("Transferencia realizada con éxito")
        else:
            print("Saldo insuficiente para realizar la transferencia")


class Cliente:
    def __init__(self, nombre, direccion, identificacion):
        self.nombre = nombre
        self.direccion = direccion
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"


class Cuenta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito realizado con éxito")

    def retirar(self, monto):
        pass

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")


class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo=0, num_retiros=0):
        super().__init__(numero, titular, saldo)
        self.num_retiros = num_retiros

    def retirar(self, monto):
        if self.num_retiros < 1:
            print("No se pueden hacer retiros en una cuenta de ahorro")
        else:
            self.saldo -= monto
            self.num_retiros -= 1
            print("Retiro realizado con éxito")


class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo=0, limite_credito=0):
        super().__init__(numero, titular, saldo)
        self.limite_credito = limite_credito

    def retirar(self, monto):
        if self.saldo + self.limite_credito < monto:
            print("No se puede hacer un retiro mayor al límite de crédito")
        else:
            self.saldo -= monto
            print("Retiro realizado con éxito")
            if self.saldo < 0:
                print("ATENCIÓN: Saldo en rojo")


# Ejemplo de uso
banco = Banco("Mi Banco", "123", "Av. Principal 123")
cliente1 = Cliente("Juan", "Calle 1", "1111")
cliente2 = Cliente("María", "Calle 2", "2222")
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)
cuenta1 = CuentaAhorro("001", cliente1, 1000, 2)
cuenta2 = CuentaCorriente("002", cliente2, 5000, 2000)
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)

cuenta1.depositar(500)
