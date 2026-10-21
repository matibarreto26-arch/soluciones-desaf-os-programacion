a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
if b != 0:  # Evito dividir entre cero.
    print("División:", a / b)
else:
    print("No puedo dividir entre cero.")
