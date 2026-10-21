from collections import Counter
import matplotlib.pyplot as plt
entrada = input("Notas separadas por comas: ")
notas = []
for texto in entrada.split(","):
    if texto.strip() != "":
        notas.append(float(texto))
if notas:
    print("Promedio:", sum(notas) / len(notas))
    print("Mínima:", min(notas), "Máxima:", max(notas))
    frecuencias = Counter(notas)  # Cuento cuántas veces aparece cada nota.
    mayor_frecuencia = max(frecuencias.values())
    modas = [nota for nota in frecuencias if frecuencias[nota] == mayor_frecuencia]  # Guardo todas las notas que empatan como más frecuentes.
    print("Notas más frecuentes:", modas, "Frecuencia:", mayor_frecuencia)
    plt.bar(list(frecuencias.keys()), list(frecuencias.values()))  # La altura de cada barra indica cuántas veces aparece esa nota.
    plt.xlabel("Nota")
    plt.ylabel("Cantidad de estudiantes")
    plt.title("Distribución de notas")
    plt.show()
else:
    print("No hay notas para analizar.")
