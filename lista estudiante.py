n = 5 
asignaturas = 3


matriznotas = []

for i in range(n):
    alumno = []
    for j in range(asignaturas):
        nota = float(input(f"Ingrese la nota de la asignatura {j+1} para el alumno {i+1}: "))
        alumno.append(nota)
    matriznotas.append(alumno)

for i, alumno in enumerate(matriznotas):
    print(f"Alumno {i+1}: Notas = {alumno}")