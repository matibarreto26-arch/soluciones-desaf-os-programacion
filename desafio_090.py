from collections import Counter
def palabras_comunes(nombre):
    contador = Counter()
    with open(nombre, "r", encoding="utf-8") as archivo:
        for linea in archivo:  # Leo de a una línea para no cargar todo el archivo.
            linea = linea.lower()
            for signo in ".,;:!?¿¡()[]{}\"'":
                linea = linea.replace(signo, " ")
            for palabra in linea.split():
                contador[palabra] += 1  # Voy contando cada palabra.
    return contador.most_common(5)  # Devuelvo las cinco más repetidas.
try:
    print(palabras_comunes(input("Archivo de texto (por ejemplo, libros.txt): ")))
except FileNotFoundError:
    print("No encontré ese archivo.")
