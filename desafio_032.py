def es_primo(numero):
    if numero < 2:  # El 0, el 1 y los negativos no son primos.
        return False
    divisor = 2
    while divisor * divisor <= numero:  # Alcanza con probar hasta la raíz cuadrada.
        if numero % divisor == 0:
            return False
        divisor += 1
    return True
def contar_primos(numeros):
    cantidad = 0
    for numero in numeros:
        if es_primo(numero):  # Uso la función anterior para contar los primos.
            cantidad += 1
    return cantidad
def main():
    numeros = [1, 2, 3, 4, 5, 9, 11]
    for numero in numeros:
        print(numero, es_primo(numero))
    print("Cantidad de primos:", contar_primos(numeros))
main()
