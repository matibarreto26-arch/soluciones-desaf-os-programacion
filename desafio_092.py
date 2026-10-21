import random
participantes = ["Ana", "Luis", "Sol", "Bruno", "Eva"]
cantidad = int(input("Cantidad de ganadores: "))
if 0 <= cantidad <= len(participantes):  # No puedo elegir más ganadores que participantes.
    ganadores = random.sample(participantes, cantidad)  # Elijo los ganadores sin repetirlos.
    print("Ganadores:", ganadores)
else:
    print("La cantidad debe estar entre cero y el total de participantes.")
