numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    tipo = "PAR"
else:
    tipo = "IMPAR"

# Determinar signo
if numero > 0:
    signo = "POSITIVO"
elif numero < 0:
    signo = "NEGATIVO"
else:
    signo = "CERO"

print("\nResultados:")
print(f"Número:     {numero}")
print(f"Tipo:       {tipo}")
print(f"Signo:      {signo}")