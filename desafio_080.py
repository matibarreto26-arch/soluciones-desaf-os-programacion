class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir(texto):
    texto = texto.strip()
    nivel = 0
    for operadores in ["+-", "*/"]:  # Busco primero las operaciones de menor prioridad.
        for i in range(len(texto) - 1, -1, -1):  # Recorro desde la derecha para respetar el orden de las restas y divisiones.
            caracter = texto[i]
            if caracter == ")":
                nivel += 1
            elif caracter == "(":
                nivel -= 1
            elif nivel == 0 and caracter in operadores:  # Solo separo por operadores que estén fuera de paréntesis.
                anterior = texto[:i].rstrip()
                if anterior == "" or anterior[-1] in "+-*/(":  # Distingo el signo de un número de una operación.
                    continue
                nodo = Nodo(caracter)
                nodo.izq = construir(texto[:i])
                nodo.der = construir(texto[i + 1:])
                return nodo
    if texto.startswith("(") and texto.endswith(")"):
        return construir(texto[1:-1])
    return Nodo(int(texto))  # Si no quedan operaciones, guardo el número.
def evaluar(nodo):
    if nodo.izq is None and nodo.der is None:
        return nodo.valor
    a = evaluar(nodo.izq)  # Calculo el resultado de la rama izquierda.
    b = evaluar(nodo.der)  # Calculo el de la derecha.
    if nodo.valor == "+":
        return a + b
    if nodo.valor == "-":
        return a - b
    if nodo.valor == "*":
        return a * b
    return a / b
expresion = "5 + 3 * 4"
arbol = construir(expresion)
print(expresion, "=", evaluar(arbol))
