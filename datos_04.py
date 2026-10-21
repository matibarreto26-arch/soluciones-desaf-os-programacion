numero = int(input("Número entero: "))
for divisor in [2, 3, 5, 7, 9, 10, 11]:
    respuesta = "Sí" if numero % divisor == 0 else "No"  # Si el resto da 0, es múltiplo.
    print(f"¿Es {numero} múltiplo de {divisor}? {respuesta}")
