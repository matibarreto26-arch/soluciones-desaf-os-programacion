class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
    def get_nombre(self):
        return self.__nombre
    def agregar_libro(self, titulo):
        if titulo not in self.__libros:
            self.__libros.append(titulo)
    def get_libros(self):
        return self.__libros.copy()  # Devuelvo una copia de la lista.

def titulos_del_autor(autor):
    return autor.get_libros()  # Accedo a los libros mediante el método de la clase.
autor = Autor("Ana")
autor.agregar_libro("Historias")
print(titulos_del_autor(autor))
