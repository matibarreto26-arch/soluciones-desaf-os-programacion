archivo = None  # Así sé si el archivo llegó a abrirse.
try:
    archivo = open(input("Nombre del archivo: "), "r", encoding="utf-8")
    print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe.")
except OSError as error:
    print("No pude acceder al archivo:", error)
finally:  # Este bloque se ejecuta aunque haya un error.
    if archivo is not None:  # Solo cierro el archivo si se abrió.
        archivo.close()
