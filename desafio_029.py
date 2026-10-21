def tienen_comunes(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True  # Con una coincidencia ya alcanza.
    return False  # Si llego hasta acá, no encontré ninguna coincidencia.
print(tienen_comunes([1, 2, 3], [3, 4]))
print(tienen_comunes([1, 2], [4, 5]))
