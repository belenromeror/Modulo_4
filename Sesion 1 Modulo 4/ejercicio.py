precios = {"camisa":30,"pantalón":50,"zapatos":80,"calcetines":10,"chaqueta":100}

for producto,precio in precios.items():
    if precio > 50:
        print(producto)

precio_total = 0
for producto,precio in precios.items():
    if producto.startswith("c"):
        precio_total += precio
print(precio_total)
