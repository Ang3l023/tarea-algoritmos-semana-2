celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        
fahrenheit = celsius * 1.8
kelvin = celsius + 273.15

print("\nResultados:")
print(f"Celsius:      {celsius} °C")
print(f"Fahrenheit:   {fahrenheit:.2f} °F")
print(f"Kelvin:       {kelvin:.2f} K")