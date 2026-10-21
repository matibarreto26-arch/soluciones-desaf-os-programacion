class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

class Poeta(Autor):
    def __init__(self, nombre, tipo_poesia):
        super().__init__(nombre)  # Uso el constructor de Autor para guardar el nombre.
        self.tipo_poesia = tipo_poesia
poeta = Poeta("Autora ficticia", "Lírica")
print(poeta.nombre, poeta.tipo_poesia)
