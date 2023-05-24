
edad = str(input("Ingresa tu edad: "))
try:
    entero = str(edad)

except ValueError:
    print("Error: Debes ingresar un número entero. Inténtalo de nuevo.")


if edad >= 18:
    print("Eres un adulto.")
else:
    print("No eres un adulto.")