try:
    with open("prestamos.txt", "r", encoding="utf-8") as archivo:
        registros = archivo.readlines()
    if not registros:
        print("No hay préstamos registrados.")
    else:
        for i, registro in enumerate(registros):
            print(i + 1, registro.strip())
        seleccion = int(input("Número del registro a eliminar: "))
        if 1 <= seleccion <= len(registros):
            registros.pop(seleccion - 1)  # Resto 1 porque el menú empieza en 1 y los índices en 0.
            with open("prestamos.txt", "w", encoding="utf-8") as archivo:  # Guardo los registros que quedaron después de eliminar.
                for registro in registros:
                    archivo.write(registro)
            print("Registro eliminado.")
        else:
            print("Ese registro no existe.")
except FileNotFoundError:
    print("Primero registrá un préstamo con el desafío 86.")
except ValueError:
    print("Ingresá el número del registro.")
