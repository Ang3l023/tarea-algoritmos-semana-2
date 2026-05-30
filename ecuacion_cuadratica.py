import math
import sys

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if a == 0:
    print("❌ Error: 'a' no puede ser cero (no sería una ecuación cuadrática).")
    sys.exit()

# Calculamos el discriminante
discriminante = b**2 - 4*a*c

print(f"\nDiscriminante (D) = {discriminante:.2f}")

if discriminante > 0:
    # Dos raíces reales diferentes
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("✅ Dos raíces reales:")
    print(f"   x1 = {raiz1:.4f}")
    print(f"   x2 = {raiz2:.4f}")
    
elif discriminante == 0:
    # Una raíz doble (real)
    raiz = -b / (2*a)
    print("✅ Una raíz real doble:")
    print(f"   x = {raiz:.4f}")
    
else:
    # Raíces complejas
    real = -b / (2*a)
    imaginario = math.sqrt(-discriminante) / (2*a)
    print("✅ Dos raíces complejas:")
    print(f"   x1 = {real:.4f} + {imaginario:.4f}i")
    print(f"   x2 = {real:.4f} - {imaginario:.4f}i")