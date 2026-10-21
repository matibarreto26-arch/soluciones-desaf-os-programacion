import numpy as np
import matplotlib.pyplot as plt
def crear_tablero(n, m):
    tablero = np.zeros((n, m), dtype=int)
    return tablero
def actualizar(tablero):
    filas, columnas = tablero.shape
    nuevo = np.zeros((filas, columnas), dtype=int)  # Guardo la siguiente generación en otra matriz.
    for fila in range(filas):
        for columna in range(columnas):
            vecinos = 0
            for df in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    f, c = fila + df, columna + dc
                    if (df != 0 or dc != 0) and 0 <= f < filas and 0 <= c < columnas:  # No cuento la propia célula ni posiciones fuera del tablero.
                        vecinos += tablero[f, c]
            if vecinos == 3 or (tablero[fila, columna] == 1 and vecinos == 2):  # Aplico las reglas de nacimiento y supervivencia.
                nuevo[fila, columna] = 1
    return nuevo
def simular(tablero, iteraciones):
    for paso in range(iteraciones + 1):
        plt.clf()
        plt.imshow(tablero, cmap="binary", vmin=0, vmax=1)
        plt.title(f"Generación {paso}")
        plt.pause(0.3)  # Hago una pausa para ver cómo cambia el tablero.
        if paso < iteraciones:
            tablero = actualizar(tablero)
    plt.show()
    return tablero
tablero = crear_tablero(7, 7)
tablero[3, 2:5] = 1  # Coloco tres células vivas como patrón inicial.
simular(tablero, 10)
