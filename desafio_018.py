inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]
print("Tipos iniciales:", len(inventario))
print("Tercer producto:", inventario[2])  # La tercera posición tiene índice 2.
inventario.remove("bananas")
inventario.extend(["frutillas", "apio", "papas"])
print("¿Hay papas?", "papas" in inventario)
while len(inventario) >= 7:  # Dejo un lugar libre para la fruta nueva.
    retirado = inventario.pop()  # Saco primero los últimos productos agregados.
    print("Retiro:", retirado)
inventario.append("dragonfruit")
inventario.sort()
copia = inventario.copy()  # Hago una copia para no cambiar el original.
print("Inventario:", inventario)
print("Copia:", copia)
