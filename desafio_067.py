try:  # Intento hacer la división y controlo los errores.
    a = int(input("Primer entero: "))
    b = int(input("Segundo entero: "))
    print("Resultado:", a / b)
except ValueError:  # Si no se ingresaron enteros, aviso.
    print("Tenés que ingresar números enteros.")
except ZeroDivisionError:  # Controlo la división entre cero.
    print("No se puede dividir entre cero.")
