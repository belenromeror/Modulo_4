salario = int(input("Ingresa el salario: "))
try:
    entero = int(salario)

except ValueError:
    print("Error: Debes ingresar un número entero. Inténtalo de nuevo.")


if salario in range(1000,2000):
    print("Salario correcto")
else:
    print("El salario no está definido en el rango")