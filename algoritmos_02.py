numeros = [3, 8, 12, 5, 0, -4]
pares = 0
for numero in numeros:
    if numero % 2 == 0:  # Si el resto es 0, el número es par.
        pares += 1
print("Cantidad de pares:", pares)
