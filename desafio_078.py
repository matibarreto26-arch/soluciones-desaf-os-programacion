class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def maximo_postorden(nodo):  # Reviso los hijos antes que la raíz.
    if nodo is None:
        return None  # La rama vacía no tiene un máximo.
    izquierda = maximo_postorden(nodo.izq)
    derecha = maximo_postorden(nodo.der)
    mayor = nodo.valor  # Empiezo con el valor del nodo, aunque sea negativo.
    if izquierda is not None and izquierda > mayor:
        mayor = izquierda
    if derecha is not None and derecha > mayor:
        mayor = derecha
    return mayor
raiz = Nodo(8)
raiz.izq = Nodo(3)
raiz.der = Nodo(10)
raiz.izq.izq = Nodo(1)
raiz.izq.der = Nodo(6)
raiz.der.der = Nodo(14)

print("Máximo:", maximo_postorden(raiz))
