cursos = {"Python", "Biología", "Matemática"}
estudiantes = {}
while True:
    nombre = input("Estudiante (ENTER para terminar): ").strip()
    if nombre == "":
        break
    curso = input("Curso completado (Python, Biología o Matemática): ").strip()
    if curso not in cursos:
        print("Ese curso no está en la oferta.")
        continue
    if nombre not in estudiantes:
        estudiantes[nombre] = set()  # Uso un conjunto para no repetir cursos.
    estudiantes[nombre].add(curso)
especifico = input("Curso para buscar estudiantes que solo completaron ese: ").strip()
for nombre, completados in estudiantes.items():
    if completados == cursos:  # Reviso si completó todos los cursos.
        print("Completó todos:", nombre)
    if completados == {especifico}:  # Busco quienes completaron solamente ese curso.
        print("Solo completó", especifico, ":", nombre)
