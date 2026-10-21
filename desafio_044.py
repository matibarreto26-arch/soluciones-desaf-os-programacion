libros = {1: {"titulo": "Libro de ejemplo", "disponible": True}}
usuarios = {1: "Ana"}
prestamos = []
multas = []
def prestar(libro_id, usuario_id):
    if libro_id not in libros or usuario_id not in usuarios:  # Compruebo que existan el libro y el usuario.
        return "Libro o usuario inexistente."
    if not libros[libro_id]["disponible"]:
        return "Libro no disponible."
    libros[libro_id]["disponible"] = False
    prestamos.append({"libro": libro_id, "usuario": usuario_id})  # Relaciono el libro con el usuario usando sus códigos.
    return "Préstamo registrado."
def multar(usuario_id, importe):
    if usuario_id in usuarios and importe > 0:
        multas.append({"usuario": usuario_id, "importe": importe})
print(prestar(1, 1))
multar(1, 25)
print("Préstamos:", prestamos, "Multas:", multas)
