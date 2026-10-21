import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
resultado = A + A.T  # Sumo la matriz y su transpuesta.
print("Rango:", np.linalg.matrix_rank(resultado))  # Calculo el rango de la matriz resultante.
