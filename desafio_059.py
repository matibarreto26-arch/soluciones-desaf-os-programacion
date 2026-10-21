class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def informacion(self):
        return f"{self.titulo} - {self.autor}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamanio_archivo):
        super().__init__(titulo, autor)  # Reutilizo los datos de Libro.
        self.formato = formato
        self.tamanio_archivo = tamanio_archivo
    def informacion(self):
        return f"{super().informacion()} - {self.formato} - {self.tamanio_archivo} MB"
class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamanio_archivo, enlace):
        super().__init__(titulo, autor, formato, tamanio_archivo)
        self.enlace = enlace
    def informacion(self):
        return f"{super().informacion()} - Descarga: {self.enlace}"  # Agrego el enlace a la información heredada.
libro = EBook("Guía", "Ana", "PDF", 2.5, "https://example.com/guia.pdf")
print(libro.informacion())
