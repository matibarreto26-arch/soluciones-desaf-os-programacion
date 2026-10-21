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
        self.autor = autor  # Relaciono el libro con el objeto Autor.
        autor.agregar_libro(self)  # Agrego este libro a la lista de su autor.

autor = Autor("Autora de ejemplo")
libro = Libro("Historias", "Cuento", "ISBN de ejemplo", autor)
print(libro.titulo, libro.autor.nombre)
