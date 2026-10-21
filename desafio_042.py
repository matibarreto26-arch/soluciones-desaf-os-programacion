def invertir_palabras(palabras):
    if len(palabras) == 0:  # La lista vacía detiene la recursión.
        return []
    return invertir_palabras(palabras[1:]) + [palabras[0]]  # Invierto el resto y dejo la primera palabra al final.
oracion = input("Oración: ")
resultado = invertir_palabras(oracion.split())
print(" ".join(resultado))
