class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def informacion(self):
        return f"{self.titulo} - {self.autor}"

class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo, nivel):
        super().__init__(titulo, autor)  # Reutilizo el constructor de Libro.
        self.campo = campo
        self.nivel = nivel
    def informacion(self):
        return f"{super().informacion()} - {self.campo} - {self.nivel}"  # Agrego los datos del libro especializado.
libro = LibroEspecializado("Introducción a las células", "Autora ficticia", "Biología", "básico")
print(libro.informacion())
