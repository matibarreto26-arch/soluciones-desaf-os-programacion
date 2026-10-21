from datetime import datetime
try:
    inicio = datetime.strptime(input("Primera fecha (AAAA-MM-DD): "), "%Y-%m-%d")  # Convierto la fecha escrita en un dato de tipo fecha.
    fin = datetime.strptime(input("Segunda fecha (AAAA-MM-DD): "), "%Y-%m-%d")
    diferencia = fin - inicio  # Resto las fechas para obtener el intervalo.
    print("Diferencia en días:", abs(diferencia.days))  # Muestro la cantidad de días sin signo negativo.
except ValueError:
    print("Ingresá fechas válidas con el formato AAAA-MM-DD.")
