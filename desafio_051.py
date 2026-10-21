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
        self.autor = autor
        autor.agregar_libro(self)
class Biblioteca:
    def __init__(self):
        self.autores = []
        self.libros = []
    def agregar_libro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)
        if libro.autor not in self.autores:
            self.autores.append(libro.autor)

def buscar_libros(biblioteca, titulo):
    return [libro for libro in biblioteca.libros if libro.titulo.lower() == titulo.lower()]  # Busco el título sin distinguir mayúsculas.
def buscar_autores(biblioteca, nombre):
    return [autor for autor in biblioteca.autores if autor.nombre.lower() == nombre.lower()]  # Hago lo mismo con el nombre del autor.
biblioteca = Biblioteca()
autor = Autor("Ana")
biblioteca.agregar_libro(Libro("Historias", "Cuento", "A001", autor))
libros = buscar_libros(biblioteca, input("Título a buscar: "))
print("Libros encontrados:", [libro.titulo for libro in libros])
autores = buscar_autores(biblioteca, input("Autor a buscar: "))
print("Autores encontrados:", [autor.nombre for autor in autores])
