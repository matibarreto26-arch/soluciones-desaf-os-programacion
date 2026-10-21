import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
resultado = 2 * A + B.T  # B.T es la transpuesta de B.
print(resultado)
