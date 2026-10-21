aprobados = 0
desaprobados = 0
notas = input("Notas separadas por comas: ").split(",")  # Separo las notas por las comas.
for texto in notas:
    nota = float(texto)
    if nota >= 7:  # En esta consigna se aprueba con 7 o más.
        aprobados += 1
    else:
        desaprobados += 1
print("Aprobaron:", aprobados)
print("Desaprobaron:", desaprobados)
