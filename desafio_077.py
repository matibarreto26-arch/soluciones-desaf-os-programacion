class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def sumar_inorden(nodo):  # Recorro izquierda, raíz y derecha.
    if nodo is None:
        return 0  # Una rama vacía no suma nada.
    izquierda = sumar_inorden(nodo.izq)
    valor = nodo.valor
    derecha = sumar_inorden(nodo.der)
    return izquierda + valor + derecha
raiz = Nodo(8)
raiz.izq = Nodo(3)
raiz.der = Nodo(10)
raiz.izq.izq = Nodo(1)
raiz.izq.der = Nodo(6)
raiz.der.der = Nodo(14)

print("Suma:", sumar_inorden(raiz))
