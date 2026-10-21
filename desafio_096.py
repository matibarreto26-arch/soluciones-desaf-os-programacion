inventario = {}
while True:  # Repito el menú hasta elegir salir.
    opcion = input("1: agregar; 2: actualizar stock; 3: buscar; 0: salir: ")
    if opcion == "0":
        break
    if opcion not in ["1", "2", "3"]:
        print("Opción incorrecta.")
        continue
    codigo = input("Código del producto: ")
    try:
        if opcion == "1":
            if codigo in inventario:
                print("Ese código ya está registrado.")
                continue
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad en stock: "))
            if precio < 0 or cantidad < 0:
                raise ValueError("El precio y el stock no pueden ser negativos.")
            inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}  # Guardo los datos de cada producto bajo su código.
            print("Producto agregado.")
        elif codigo not in inventario:
            print("Producto no encontrado.")
        elif opcion == "2":
            cantidad = int(input("Nueva cantidad en stock: "))
            if cantidad < 0:
                raise ValueError("El stock no puede ser negativo.")
            inventario[codigo]["cantidad"] = cantidad  # Reemplazo el stock por la nueva cantidad.
            print("Stock actualizado.")
        else:
            print(inventario[codigo])
    except ValueError as error:  # Controlo los datos numéricos incorrectos.
        print("Dato incorrecto:", error)
