import random
autos = ["Auto 1", "Auto 2", "Auto 3"]
velocidades = [random.randint(1, 10) for auto in autos]  # Cada auto mantiene la velocidad que le tocó.
distancias = [0, 0, 0]
print("Velocidades:", velocidades)
for segundo in range(10):  # Cada vuelta representa un segundo.
    for i in range(len(autos)):
        distancias[i] += velocidades[i]
    print(f"Segundo {segundo + 1}: {distancias}")
mayor = max(distancias)
for i in range(len(autos)):
    if distancias[i] == mayor:  # Así muestro también los empates.
        print("Ganador:", autos[i])
