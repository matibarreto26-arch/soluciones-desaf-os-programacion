def buscar_calificacion(tabla, nota):
    resultados = []
    for fila in range(len(tabla)):
        for columna in range(len(tabla[fila])):
            if tabla[fila][columna] == nota:
                resultados.append((fila, columna))  # Guardo la fila y la columna de cada coincidencia.
    return resultados
estudiantes = ["Ana", "Luis", "Sol"]
materias = ["Biología", "Matemática", "Historia"]
tabla = [[8, 7, 9], [6, 8, 7], [10, 9, 8]]
resultados = buscar_calificacion(tabla, float(input("Nota a buscar: ")))
for fila, columna in resultados:
    print(estudiantes[fila], materias[columna])  # Relaciono esas posiciones con el estudiante y la materia.
if not resultados:
    print("No se encontró esa nota.")
