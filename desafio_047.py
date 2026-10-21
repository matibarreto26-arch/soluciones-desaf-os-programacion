class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Cada autor tiene su propia lista de libros.
    def agregar_libro(self, libro):
        if libro not in self.libros:  # Evito agregar el mismo libro dos veces.
            self.libros.append(libro)
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

autor = Autor("Autora de ejemplo")
autor.agregar_libro("Primer libro")
autor.agregar_libro("Segundo libro")
autor.eliminar_libro("Primer libro")
print(autor.nombre, autor.libros)
