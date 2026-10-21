class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:  # Los menores van a la izquierda.
        nodo.izq = insertar(nodo.izq, valor)
    elif valor > nodo.valor:  # Los mayores van a la derecha.
        nodo.der = insertar(nodo.der, valor)
    return nodo  # Si el valor ya existe, no lo agrego otra vez.
def buscar(nodo, valor):
    if nodo is None:
        return False
    if valor == nodo.valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izq, valor)
    return buscar(nodo.der, valor)
raiz = None
for valor in [8, 3, 10, 1, 6, 14]:
    raiz = insertar(raiz, valor)
print(buscar(raiz, int(input("Número a buscar: "))))
