import procesador_texto  # Uso las funciones del archivo auxiliar.
texto = input("Texto: ")
palabra = input("Palabra a resaltar: ")
try:
    print(procesador_texto.resaltar(texto, palabra))
except RecursionError:  # Controlo si el texto exige demasiadas llamadas recursivas.
    print("El texto supera el límite de recursión; probá con un fragmento menor.")
