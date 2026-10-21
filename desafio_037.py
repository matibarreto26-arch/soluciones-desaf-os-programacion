from collections import Counter
import matplotlib.pyplot as plt
texto = input("Texto: ").lower()
for signo in ".,;:!?¿¡()[]{}\"'":
    texto = texto.replace(signo, " ")  # Saco los signos para no contarlos como parte de las palabras.
frecuencias = Counter(texto.split())  # Cuento las palabras.
comunes = frecuencias.most_common(10)  # Busco las diez más repetidas.
for palabra, cantidad in comunes:
    print(palabra, cantidad)
if comunes:
    palabras = [dato[0] for dato in comunes]
    cantidades = [dato[1] for dato in comunes]
    plt.bar(palabras, cantidades)
    plt.xticks(rotation=45)
    plt.ylabel("Frecuencia")
    plt.show()
