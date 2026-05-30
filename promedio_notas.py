print("promedio notas")
#notas de estudiantes
nota1 = float(input("Ingrese la primera nota (0<20): "))
nota2 = float(input("Ingrese la segunda nota (0<20): "))
nota3 = float(input("Ingrese la tercera nota (0<20): "))    
#escala calculo dee rango notas
if not ( 0 <= nota1 <= 20 and 0 <= nota2 <= 20 and 0 <= nota3 <= 20):
    print("Error: Las notas deben estar entre 0 y 20.")
    exit()
#calcular el promeedio
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es: {promedio:.2f}")
#si el promedio es mayor o igual a 11, el estudiante esta aprobado, de lo contrario esta aprobado 
if promedio >= 11:
#imprimir el resultado
    print("El estudiante está aprobado.")
else:
    print("El estudiante está desaprobado.")