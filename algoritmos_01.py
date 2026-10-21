n = int(input("Cantidad de números naturales: "))
if n < 0:
    print("Ingresá un entero mayor o igual que cero.")
else:
    suma = 0
    for numero in range(1, n + 1):  # Pongo n + 1 para incluir el último número.
        suma += numero  # Voy sumando los números.
    print("Suma:", suma)
