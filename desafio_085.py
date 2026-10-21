class Nodo:
    def __init__(self, promedio, nombre):
        self.promedio = promedio
        self.estudiantes = [nombre]  # Agrupo los nombres que tengan el mismo promedio.
        self.izq = None
        self.der = None
def insertar(nodo, nombre, promedio):
    if nodo is None:
        return Nodo(promedio, nombre)
    if promedio < nodo.promedio:
        nodo.izq = insertar(nodo.izq, nombre, promedio)
    elif promedio > nodo.promedio:
        nodo.der = insertar(nodo.der, nombre, promedio)
    else:
        nodo.estudiantes.append(nombre)  # Si empatan, los guardo en el mismo nodo.
    return nodo
def inorden(nodo):  # Este recorrido muestra los promedios de menor a mayor.
    if nodo is not None:
        inorden(nodo.izq)
        print(nodo.promedio, nodo.estudiantes)
        inorden(nodo.der)
raiz = None
for nombre, promedio in [("Ana", 8), ("Luis", 6), ("Sol", 10), ("Bruno", 8)]:
    raiz = insertar(raiz, nombre, promedio)
inorden(raiz)
