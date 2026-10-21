import numpy as np
A = np.array([[1, 0, 1], [4, -1, 4], [5, 6, 7]])
inversa = np.linalg.inv(A)  # Calculo la inversa de la matriz.
print("Traza:", np.trace(inversa))  # Sumo los valores de la diagonal.
