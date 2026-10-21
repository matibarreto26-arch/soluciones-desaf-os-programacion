traducciones = {
    "hello": {"es": "hola", "fr": "bonjour", "pt": "olá", "it": "ciao", "de": "hallo"},
    "world": {"es": "mundo", "fr": "monde", "pt": "mundo", "it": "mondo", "de": "Welt"},
    "goodbye": {"es": "adiós", "fr": "au revoir", "pt": "adeus", "it": "arrivederci", "de": "auf Wiedersehen"}
}

def traducir(palabra, idiomas):
    resultado = {}
    for idioma in idiomas:
        try:
            resultado[idioma] = traducciones[palabra][idioma]  # Busco la palabra y luego el idioma.
        except KeyError:  # Controlo si falta la palabra o la traducción.
            resultado[idioma] = "Traducción no encontrada"
    return resultado
palabra = input("Palabra en inglés: ").lower()
idiomas = input("Idiomas separados por espacios (es fr pt it de): ").lower().split()
print(traducir(palabra, idiomas))
