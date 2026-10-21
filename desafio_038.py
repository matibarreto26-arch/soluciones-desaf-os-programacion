import os
nombre = "texto_procesador.txt"
opcion = input("1: guardar texto nuevo; 2: leer texto: ")
if opcion == "1":
    texto = input("Texto: ")
    with open(nombre, "a", encoding="utf-8") as archivo:  # Uso a para agregar texto sin borrar lo anterior.
        archivo.write(texto + "\n")
    print("Texto guardado.")
elif opcion == "2":
    if os.path.exists(nombre):  # Reviso que el archivo exista antes de leerlo.
        with open(nombre, "r", encoding="utf-8") as archivo:
            print(archivo.read())
    else:
        print("Todavía no hay texto guardado.")
else:
    print("Opción incorrecta.")
