a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
if a == b or a == c or b == c:  # Reviso que los tres sean distintos.
    print("La consigna pide tres números distintos.")
elif a < b < c:  # Comparo los números para mostrarlos de menor a mayor.
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)
