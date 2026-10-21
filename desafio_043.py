def contar_manzanas(n):  # Tomo el conteo como 1 + 2 + ... + n.
    if n <= 0:  # Acá termina la recursión.
        return 0
    return n + contar_manzanas(n - 1)  # Sumo el conteo actual a los anteriores.
n = int(input("Cantidad de manzanas: "))
if n < 0:
    print("La cantidad no puede ser negativa.")
else:
    print("Total acumulado:", contar_manzanas(n))
