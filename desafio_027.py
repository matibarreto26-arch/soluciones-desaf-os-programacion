def calcular(numeros):
    if len(numeros) == 0:
        return 0, None  # Sin números no puedo calcular el promedio.
    suma = sum(numeros)
    return suma, suma / len(numeros)  # Devuelvo los dos resultados juntos.
suma, promedio = calcular([4, 6, 8])
print("Suma:", suma, "Promedio:", promedio)
