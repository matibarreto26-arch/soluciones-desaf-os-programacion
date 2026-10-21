cantidad_productos = int(input("Cantidad de productos diferentes: "))
lineas = []
total = 0
for i in range(cantidad_productos):
    nombre = input("Producto: ")
    cantidad = int(input("Unidades: "))
    precio = float(input("Precio unitario: "))
    subtotal = cantidad * precio  # Multiplico las unidades por el precio.
    total += subtotal
    lineas.append(f"{nombre:<20} {cantidad:>5} {precio:>10.2f} {subtotal:>10.2f}")  # Dejo las columnas alineadas y los precios con dos decimales.
print(f"{'Producto':<20} {'Cant.':>5} {'Precio':>10} {'Subtotal':>10}")
for linea in lineas:
    print(linea)
print(f"TOTAL: {total:.2f}")
