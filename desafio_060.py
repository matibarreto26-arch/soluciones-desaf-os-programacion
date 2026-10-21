class Academico:
    def __init__(self, universidad):
        super().__init__()
        self.universidad = universidad
class Escritor:
    def __init__(self, nombre, genero, universidad):
        super().__init__(universidad)  # En esta jerarquía, la siguiente clase es Academico.
        self.nombre = nombre
        self.genero = genero
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        super().__init__(nombre, genero, universidad)  # Inicio la cadena de constructores de las clases base.
        self.articulos = []
    def publicar_articulo(self, titulo):
        self.articulos.append(titulo)
autor = EscritorAcademico("Autor ficticio", "Ensayo", "Universidad de ejemplo")
autor.publicar_articulo("Aprender programación")
print(autor.nombre, autor.genero, autor.universidad, autor.articulos)
