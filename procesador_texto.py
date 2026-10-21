def negrita(texto):
    return "**" + texto + "**"  # Agrego las marcas de negrita de Markdown.
def italica(texto):
    return "*" + texto + "*"  # Agrego las marcas de cursiva.
def resaltar(texto, palabra, inicio=0):
    if palabra == "":  # Evito buscar una palabra vacía.
        return texto
    posicion = texto.find(palabra, inicio)  # Busco la siguiente aparición desde esa posición.
    if posicion == -1:
        return texto[inicio:]
    fin = posicion + len(palabra)
    antes_valido = posicion == 0 or not texto[posicion - 1].isalnum()  # Reviso que no sea parte de otra palabra.
    despues_valido = fin == len(texto) or not texto[fin].isalnum()
    fragmento = texto[posicion:fin]
    if antes_valido and despues_valido:
        fragmento = negrita(fragmento)
    return texto[inicio:posicion] + fragmento + resaltar(texto, palabra, fin)  # Sigo buscando desde el final de esta coincidencia.
