estudiantes = [("Ana", 8), ("Luis", 6), ("Sol", 10), ("Bruno", 9)]
for i in range(len(estudiantes)):
    mayor = i  # Busco el mayor promedio entre los que faltan ordenar.
    for j in range(i + 1, len(estudiantes)):
        if estudiantes[j][1] > estudiantes[mayor][1]:
            mayor = j
    estudiantes[i], estudiantes[mayor] = estudiantes[mayor], estudiantes[i]  # Intercambio las posiciones para dejar el mayor primero.
print(estudiantes)
