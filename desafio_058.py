class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
class Bibliotecario(Usuario):
    def __init__(self, nombre, seccion, anios_experiencia):
        super().__init__(nombre)  # Reutilizo el constructor de Usuario.
        self.seccion = seccion
        self.anios_experiencia = anios_experiencia
bibliotecario = Bibliotecario("Ana", "Ciencias", 5)
print(bibliotecario.nombre, bibliotecario.seccion, bibliotecario.anios_experiencia)
