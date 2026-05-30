#Calculadora de IMC y diagnosticos 

##Entrada de datos
peso = float(input("Ingrese su peso en kg: "))
talla = float(input("Ingrese su talla en metros: "))
#Uso float () ya que el peso y la talla contienen num enteros o decimales


##Parte1 Calcular el IMC
imc = peso / (talla **2)

##Parte2 Mostrar el resultado del IMC con dos decimales
print("Su IMC es:", imc)

##Parte3 Diagnosticar el estado de salud según el IMC
#Mediante estas 6 condiciones se asigna el dx que hacen una comparativa de imc 
if imc < 18.5:
    print("Bajo peso")

elif imc < 25:
    print("Normal")

elif imc < 30:
    print("Sobrepeso")

elif imc < 35:
    print("Obesidad I")

elif imc < 40:
    print("Obesidad II")

else:
    print("Obesidad III")

