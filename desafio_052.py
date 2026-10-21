class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo  # Uso doble guion bajo para el atributo interno.
        self.__autor = autor
        self.__isbn = isbn
    def get_titulo(self):  # Con el getter consulto el dato.
        return self.__titulo
    def set_titulo(self, titulo):  # Con el setter puedo cambiarlo.
        self.__titulo = titulo
    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor
    def get_isbn(self):
        return self.__isbn
    def set_isbn(self, isbn):
        self.__isbn = isbn
libro = Libro("Borrador", "Ana", "A001")
libro.set_titulo("Versión final")
libro.set_autor("Ana Pérez")
libro.set_isbn("A002")
print(libro.get_titulo(), libro.get_autor(), libro.get_isbn())
