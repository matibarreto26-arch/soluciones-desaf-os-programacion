astronomia = set(["Ana", "Luis", "Sol"])
matematica = set(["Luis", "Sol", "Eva"])
programacion = set(["Sol", "Ana", "Bruno"])
print("En todos:", astronomia.intersection(matematica, programacion))  # La intersección muestra quiénes participaron en los tres.
print("Solo programación:", programacion.difference(astronomia.union(matematica)))  # Quito quienes también estuvieron en otros concursos.
print("Participantes únicos:", astronomia.union(matematica, programacion))  # La unión reúne a todos sin repetirlos.
