valores = [2, 0, "4", "hola", None]  # Uso distintos datos para probar los errores.
for valor in valores:
    try:
        numero = float(valor)  # La conversión puede fallar por el tipo o por el valor.
        print("10 dividido entre", valor, "es", 10 / numero)
    except ZeroDivisionError:
        print("No puedo dividir entre cero.")
    except TypeError:
        print("Tipo de dato no compatible:", valor)
    except ValueError:
        print("Valor no numérico:", valor)
