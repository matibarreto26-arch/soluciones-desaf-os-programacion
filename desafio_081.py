class Grupo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.hijos = []
def recorrer_niveles(raiz):
    pendientes = [raiz]  # Uso una lista como cola.
    while pendientes:
        grupo = pendientes.pop(0)  # Saco el primero para recorrer por niveles.
        print("Grado", grupo.grado, grupo.estudiantes)
        pendientes.extend(grupo.hijos)  # Dejo sus hijos al final de la cola.
raiz = Grupo(12, ["Ana", "Luis"])
actual = raiz
for grado in range(11, 0, -1):
    siguiente = Grupo(grado, [f"Estudiante de grado {grado}"])
    actual.hijos.append(siguiente)
    actual = siguiente
recorrer_niveles(raiz)
