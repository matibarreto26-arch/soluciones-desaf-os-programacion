import random
import string
caracteres = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits)]  # Aseguro una minúscula, una mayúscula y un número.
opciones = string.ascii_letters + string.digits
for i in range(5):
    caracteres.append(random.choice(opciones))
random.shuffle(caracteres)  # Mezclo los caracteres para cambiar su orden.
contrasena = "".join(caracteres)  # Uno los caracteres en un solo texto.
print("Contraseña de práctica:", contrasena)
