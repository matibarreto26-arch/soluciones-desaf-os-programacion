torneos = [{"Ana", "Luis", "Sol"}, {"Luis", "Sol", "Eva"}, {"Sol", "Bruno"}]
en_todos = torneos[0].copy()  # Hago una copia para no cambiar el primer conjunto.
unicos = set()
for torneo in torneos:
    en_todos = en_todos.intersection(torneo)
    unicos = unicos.union(torneo)
exclusivos = set()
for atleta in unicos:
    cantidad = 0
    for torneo in torneos:
        if atleta in torneo:
            cantidad += 1
    if cantidad == 1:  # Busco atletas que estuvieron en un solo torneo.
        exclusivos.add(atleta)
print("En todos:", en_todos)
print("En un único torneo:", exclusivos)
print("Total de atletas distintos:", len(unicos))
