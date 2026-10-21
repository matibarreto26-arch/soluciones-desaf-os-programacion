libro = input("Nombre del libro: ")
prestatario = input("Nombre del prestatario: ")
fecha = input("Fecha del préstamo (AAAA-MM-DD): ")
with open("prestamos.txt", "a", encoding="utf-8") as archivo:  # Uso a para agregar préstamos sin borrar los anteriores.
    archivo.write(f"{libro};{prestatario};{fecha}\n")  # Separo los datos con punto y coma y dejo un préstamo por línea.
print("Préstamo registrado.")
