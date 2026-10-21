class Autor:
    def __init__(self, nombre, nacionalidad, anio_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.anio_nacimiento = anio_nacimiento
        self.premios = []  # Dejo una lista para agregar premios después.
    def agregar_premio(self, premio):
        self.premios.append(premio)
    def biografia(self):
        return f"{self.nombre}, {self.nacionalidad}, nació en {self.anio_nacimiento}. Premios: {self.premios}"
autor = Autor("Autor ficticio", "Uruguaya", 1980)
autor.agregar_premio("Premio del taller")
print(autor.biografia())
