import sys

tasas = {
    'PEN': 1.0,
    'USD': 3.75,
    'EUR': 4.10
}

print("Monedas disponibles:")
print("1. Soles (PEN)")
print("2. Dólares (USD)")
print("3. Euros (EUR)")

origen = input("\nSeleccione moneda de origen (PEN/USD/EUR): ").strip().upper()
if origen not in tasas:
    print("❌ Moneda no válida.")
    sys.exit()

# Selección de moneda destino
destino = input("Seleccione moneda de destino (PEN/USD/EUR): ").strip().upper()
if destino not in tasas:
    print("❌ Moneda no válida.")
    sys.exit()

if origen == destino:
    print("❌ Las monedas deben ser diferentes.")
    sys.exit()

monto = float(input(f"Ingrese la cantidad en {origen}: "))

monto_en_pen = monto * tasas[origen]
monto_final = monto_en_pen / tasas[destino]

print(f"\n✅ Resultado:")
print(f"{monto:.2f} {origen} = {monto_final:.2f} {destino}")