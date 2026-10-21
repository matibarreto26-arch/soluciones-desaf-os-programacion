suma = 0
for i in range(5):
    nota = float(input(f"Nota {i + 1}: "))  # Uso float porque la nota puede tener decimales.
    suma += nota
print("Promedio:", suma / 5)  # Divido la suma entre las cinco notas.
