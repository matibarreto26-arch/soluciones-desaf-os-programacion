original = [1, 3, 2, 3, 1, 5, 2]
sin_duplicados = []
for numero in original:
    if numero not in sin_duplicados:  # Agrego el número solo si todavía no está.
        sin_duplicados.append(numero)
print("Original:", original)
print("Sin duplicados:", sin_duplicados)
