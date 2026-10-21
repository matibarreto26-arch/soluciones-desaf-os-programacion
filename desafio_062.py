class Musico:
    def instrumento(self):
        return "Instrumento sin especificar"
class Guitarrista(Musico):
    def instrumento(self):
        return "Guitarra"
class Baterista(Musico):
    def instrumento(self):
        return "Batería"
for musico in [Guitarrista(), Baterista()]:
    print(musico.instrumento())  # La misma llamada da un resultado distinto según el objeto.
