entrada = input("Notas separadas por comas: ")
if entrada.strip() == "":  # Reviso que se haya escrito alguna nota.
    print("No ingresaste notas.")
else:
    notas = entrada.split(",")
    suma = 0
    for nota in notas:
        suma += float(nota)
    print("Promedio:", suma / len(notas))  # Divido entre la cantidad de notas ingresadas.
