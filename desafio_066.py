class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def resultado(self):
        return None
class Suma(Operacion):
    def resultado(self):
        return self.a + self.b
class Multiplicacion(Operacion):
    def resultado(self):
        return self.a * self.b
for operacion in [Suma(3, 4), Multiplicacion(3, 4)]:
    print(operacion.resultado())  # Cada objeto resuelve la operación que le corresponde.
