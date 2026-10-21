registros = [("Ciudad A", 22.5, 70), ("Ciudad B", 18.0, 80), ("Ciudad C", 25.0, 65)]
mas_calida = registros[0]
mas_fria = registros[0]
humedad_total = 0
for registro in registros:
    ciudad, temperatura, humedad = registro  # Separo los datos de la tupla.
    humedad_total += humedad
    if temperatura > mas_calida[1]:
        mas_calida = registro
    if temperatura < mas_fria[1]:
        mas_fria = registro
print("Más cálida:", mas_calida[0], mas_calida[1])
print("Más fría:", mas_fria[0], mas_fria[1])
print("Humedad promedio:", humedad_total / len(registros))  # Calculo la humedad promedio de los registros.
