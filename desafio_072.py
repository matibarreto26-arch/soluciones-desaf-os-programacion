codigos = [101, 104, 108, 115]
codigo = int(input("Código a buscar: "))
if codigo in codigos:
    print("Índice:", codigos.index(codigo))  # Las posiciones empiezan en 0.
else:
    print("Código no encontrado.")
