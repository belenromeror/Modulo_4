suma = 3000
contador = 0

"Division por 0"
try:
    resultado = suma/contador
    print(resultado)

except ZeroDivisionError as e:
    print("División por cero")

