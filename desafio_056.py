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
        return self.__libros.copy()

def autor_con_mas_libros(autores):
    if not autores:  # Reviso si la lista está vacía.
        return None
    mayor = autores[0]
    for autor in autores[1:]:
        if len(autor.get_libros()) > len(mayor.get_libros()):  # Comparo la cantidad de libros usando los métodos.
            mayor = autor
    return mayor  # Si hay empate, queda el primero que encontré.
ana = Autor("Ana")
luis = Autor("Luis")
ana.agregar_libro("Historias")
luis.agregar_libro("Viajes")
luis.agregar_libro("Caminos")
resultado = autor_con_mas_libros([ana, luis])
print(resultado.get_nombre())
