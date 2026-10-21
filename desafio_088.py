import csv
try:
    with open("inventario.csv", "r", newline="", encoding="utf-8") as archivo:
        filas = list(csv.reader(archivo))  # Guardo las filas para poder modificarlas.
    titulo = input("Título del libro: ")
    cantidad = int(input("Nueva cantidad de copias: "))
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    encontrado = False
    for fila in filas[1:]:  # Salto la primera fila porque tiene los encabezados.
        if fila[0].lower() == titulo.lower():
            fila[1] = str(cantidad)
            encontrado = True
    if encontrado:
        with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:  # Vuelvo a escribir el archivo con los datos actualizados.
            escritor = csv.writer(archivo)
            for fila in filas:
                escritor.writerow(fila)
        print("Inventario actualizado.")
    else:
        print("Libro no encontrado.")
except FileNotFoundError:
    print("Falta el archivo inventario.csv incluido con las soluciones.")
except ValueError as error:
    print("Cantidad incorrecta:", error)
