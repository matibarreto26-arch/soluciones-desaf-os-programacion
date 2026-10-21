class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def preorden(nodo):  # Recorro raíz, izquierda y derecha.
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izq)
        preorden(nodo.der)
raiz = Nodo(8)
raiz.izq = Nodo(3)
raiz.der = Nodo(10)
raiz.izq.izq = Nodo(1)
raiz.izq.der = Nodo(6)
raiz.der.der = Nodo(14)

preorden(raiz)
