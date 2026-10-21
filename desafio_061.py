class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
class Administrador:
    def administrar(self):
        return "Organizo los recursos."
class Mantenimiento:
    def reparar(self):
        return "Reviso los equipos."
class Capacitador:
    def capacitar(self):
        return "Capacito al equipo."
class Gerente(Empleado, Capacitador):  # Heredo características de las dos clases.
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rol = Administrador()  # Uso composición: el gerente contiene otro objeto.
class Tecnico(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rol = Mantenimiento()  # El técnico tiene un objeto para su rol de mantenimiento.
class Voluntario(Empleado):
    def ayudar(self):
        return "Ayudo a ordenar los libros."
gerente = Gerente("Ana")
tecnico = Tecnico("Luis")
voluntario = Voluntario("Sol")
print(gerente.nombre, gerente.capacitar(), gerente.rol.administrar())
print(tecnico.nombre, tecnico.rol.reparar())
print(voluntario.nombre, voluntario.ayudar())
