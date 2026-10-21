def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")  # No tengo en cuenta mayúsculas ni espacios.
    return texto == texto[::-1]  # Comparo con el texto al revés.
print(es_palindromo(input("Palabra o frase: ")))
