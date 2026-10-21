import math
class NegativeNumberError(Exception):  # Creo mi propia excepción.
    pass
try:
    numero = float(input("Número para calcular su raíz: "))
    if numero < 0:
        raise NegativeNumberError("No puedo calcular una raíz real de un número negativo.")  # La activo si el número es negativo.
    print("Raíz cuadrada:", math.sqrt(numero))
except NegativeNumberError as error:
    print(error)
except ValueError:
    print("Ingresá un valor numérico.")
