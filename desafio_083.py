def buscar(estudiantes, nombre):
    bajo = 0
    alto = len(estudiantes) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Busco el centro de la parte que queda por revisar.
        if estudiantes[medio] == nombre:
            return medio
        elif estudiantes[medio] < nombre:
            bajo = medio + 1  # Descarto la mitad anterior.
        else:
            alto = medio - 1  # Descarto la mitad posterior.
    return -1  # Uso -1 para indicar que no lo encontré.
estudiantes = ["Ana", "Bruno", "Carlos", "Lucia", "Sofia"]
resultado = buscar(estudiantes, input("Nombre con su mayúscula inicial: "))
if resultado == -1:
    print("Estudiante no encontrado.")
else:
    print("Índice:", resultado)
