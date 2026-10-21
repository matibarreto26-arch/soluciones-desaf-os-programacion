class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
    def biografia(self):
        return f"Autor: {self.nombre}"
class Escritor(Autor):
    def biografia(self):
        return super().biografia() + ". Se dedica a la escritura."  # Amplío la biografía de la clase base.
escritor = Escritor("Ana")
print(escritor.biografia())
print(Autor.biografia(escritor))  # Llamo directamente a la versión de Autor.
