def mcd(a, b):
    if b == 0:  # Este caso detiene la recursión.
        return abs(a)
    return mcd(b, a % b)  # Vuelvo a llamar a la función con el divisor y el resto.
print("MCD:", mcd(8, 12))
