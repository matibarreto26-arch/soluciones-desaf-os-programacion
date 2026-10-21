def iniciales_mayusculas(texto):
    palabras = texto.split()
    resultado = []
    for palabra in palabras:
        resultado.append(palabra[0].upper() + palabra[1:])  # Cambio solo la primera letra de cada palabra.
    return " ".join(resultado)  # Vuelvo a unir las palabras con espacios.
print(iniciales_mayusculas(input("Texto: ")))
