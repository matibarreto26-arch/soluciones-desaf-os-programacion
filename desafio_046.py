tiendas = {}
def crear_tienda(nombre):
    tiendas[nombre] = {"productos": {}, "empleados": [], "transacciones": []}  # Cada tienda tiene sus propios datos.
def vender(nombre, producto, cantidad):
    tienda = tiendas[nombre]
    if producto not in tienda["productos"]:
        return "Producto inexistente."
    if cantidad <= 0 or cantidad > tienda["productos"][producto]:  # Reviso que haya unidades suficientes para la venta.
        return "Cantidad inválida o stock insuficiente."
    tienda["productos"][producto] -= cantidad  # Descuento las unidades vendidas.
    tienda["transacciones"].append((producto, cantidad))
    return "Venta registrada."
crear_tienda("Centro")
crear_tienda("Barrio")
tiendas["Centro"]["productos"]["Cuaderno"] = 10
tiendas["Centro"]["empleados"].append("Ana")
print(vender("Centro", "Cuaderno", 3))
print(tiendas)
