import math
class Figura:
    def area(self):
        return None
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2  # Calculo el área del círculo.
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
for figura in [Circulo(2), Cuadrado(3)]:
    print("Área:", figura.area())  # Cada figura usa su propia fórmula.
