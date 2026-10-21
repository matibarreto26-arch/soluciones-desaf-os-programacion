ventas = [("A", 2, 100), ("B", 1, 250), ("A", 3, 100), ("B", 4, 250)]
ingreso = 0
cantidades = {}
for producto, cantidad, precio in ventas:
    ingreso += cantidad * precio  # Sumo lo generado por cada venta.
    if producto not in cantidades:
        cantidades[producto] = 0
    cantidades[producto] += cantidad  # Acumulo las unidades vendidas de cada producto.
print("Ingreso total:", ingreso)
if cantidades:
    mayor = max(cantidades.values())
    for producto, cantidad in cantidades.items():
        if cantidad == mayor:  # Incluyo también los empates.
            print("Más vendido:", producto, "Unidades:", cantidad)
