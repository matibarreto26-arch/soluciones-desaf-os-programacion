class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
    @property  # Permite consultar el dato como un atributo.
    def nombre(self):
        return self.__nombre
    @nombre.setter  # Se ejecuta cuando asigno un nombre nuevo.
    def nombre(self, valor):
        self.__nombre = valor
    @property
    def nacionalidad(self):
        return self.__nacionalidad
    @nacionalidad.setter  # Permite cambiar la nacionalidad.
    def nacionalidad(self, valor):
        self.__nacionalidad = valor
autor = Autor("Ana", "Uruguaya")
autor.nombre = "Ana Pérez"
print(autor.nombre, autor.nacionalidad)
