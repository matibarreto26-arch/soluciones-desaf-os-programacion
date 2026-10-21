def buscar_libros(autor):
    encontrados = []
    with open("libros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            titulo, nombre = linea.strip().split(";")  # Separo el título y el autor por el punto y coma.
            if nombre.lower() == autor.lower():  # Comparo sin distinguir mayúsculas.
                encontrados.append(titulo)
    return encontrados
try:
    libros = buscar_libros(input("Autor a buscar: ").strip())
    if libros:
        for libro in libros:
            print(libro)
    else:
        print("No hay libros de ese autor.")
except FileNotFoundError:
    print("Colocá libros.txt en la carpeta desde la que ejecutás el programa.")
