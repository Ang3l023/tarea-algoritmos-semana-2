import math
import sys

radio = float(input("Ingrese el radio del círculo: "))
        
if radio < 0:
    print("❌ El radio no puede ser negativo.")
    sys.exit()

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print("\nResultados:")
print(f"Radio:           {radio}")
print(f"Área:            {area:.2f}")
print(f"Perímetro (C):   {perimetro:.2f}")