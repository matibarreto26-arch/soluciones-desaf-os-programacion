class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    def agregar_libro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor  # Guardo la relación entre el libro y el autor.
        autor.agregar_libro(self)
class Biblioteca:
    def __init__(self):
        self.autores = []
        self.libros = []
    def agregar_libro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)
        if libro.autor not in self.autores:  # Registro al autor si todavía no estaba en la biblioteca.
            self.autores.append(libro.autor)

biblioteca = Biblioteca()
autor = Autor("Autora de ejemplo")
autor2 = Autor("Otro autor")
biblioteca.agregar_libro(Libro("Historias", "Cuento", "A001", autor))
biblioteca.agregar_libro(Libro("Viajes", "Novela", "A002", autor2))
for libro in biblioteca.libros:
    print(libro.titulo, libro.autor.nombre)
