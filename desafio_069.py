def factorial(numero):
    if type(numero) != int:  # Compruebo que el dato sea entero.
        raise TypeError("El número debe ser entero.")
    if numero < 0:
        raise ValueError("El número no puede ser negativo.")
    if numero > 1000:  # Elijo 1000 como límite para este programa.
        raise ValueError("El límite elegido para este programa es 1000.")
    resultado = 1  # Empiezo en 1 para multiplicar; también sirve para 0!.
    for factor in range(1, numero + 1):
        resultado *= factor
    return resultado
try:
    numero = int(input("Entero de 0 a 1000: "))
    print("Factorial:", factorial(numero))
except (ValueError, TypeError) as error:
    print("Error:", error)
