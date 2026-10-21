def crear_personaje(nombre, tipo, arma):
    return {"nombre": nombre, "tipo": tipo, "arma": arma, "habilidades": []}  # Guardo los datos del personaje juntos.
def agregar_habilidad(personaje, habilidad):
    if habilidad not in personaje["habilidades"]:  # Evito repetir una habilidad.
        personaje["habilidades"].append(habilidad)
def atacar(personaje):
    print(personaje["nombre"], "ataca con", personaje["arma"])
personaje = crear_personaje("Luna", "Arquera", "Arco")
agregar_habilidad(personaje, "Disparo preciso")
atacar(personaje)
print(personaje)
