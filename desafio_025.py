import numpy as np
import random
tablero = np.zeros((5, 5), dtype=int)  # El 0 representa agua y el 1 un barco.
barcos = 0
while barcos < 3:
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if tablero[x, y] == 0:  # Evito poner dos barcos en el mismo lugar.
        tablero[x, y] = 1
        barcos += 1
def disparar(x, y):
    if not (0 <= x < 5 and 0 <= y < 5):  # Reviso que el disparo quede dentro del tablero.
        print("Coordenadas fuera del tablero.")
    elif tablero[x, y] == 1:
        print("¡Golpeaste un barco!")
    else:
        print("El disparo cayó al agua.")
x = int(input("Fila de 0 a 4: "))
y = int(input("Columna de 0 a 4: "))
disparar(x, y)
