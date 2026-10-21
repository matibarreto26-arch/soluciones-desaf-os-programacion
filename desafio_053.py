class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []  # Guardo la lista dentro del objeto.
    def get_nombre(self):
        return self.__nombre
    def agregar_libro(self, titulo):
        if titulo not in self.__libros:
            self.__libros.append(titulo)
    def get_libros(self):
        return self.__libros.copy()  # Devuelvo una copia para no exponer la lista original.

autor = Autor("Ana")
autor.agregar_libro("Historias")
print(autor.get_libros())
