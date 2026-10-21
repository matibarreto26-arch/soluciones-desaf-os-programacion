def mcd(a, b):
    a, b = abs(a), abs(b)  # Trabajo con valores positivos o cero.
    while b != 0:
        a, b = b, a % b  # Repito el cálculo con el divisor y el resto.
    return a
print("MCD:", mcd(48, 18))
