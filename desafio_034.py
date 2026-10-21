import string
texto = input("Texto: ")
print(string.capwords(texto))  # Pongo las iniciales en mayúscula.
plantilla = string.Template("Texto recibido: $contenido")
print(plantilla.substitute(contenido=texto))  # Reemplazo el marcador por el texto ingresado.
formateador = string.Formatter()
print(formateador.format("Cantidad de caracteres: {}", len(texto)))  # Completo el mensaje con la cantidad de caracteres.
