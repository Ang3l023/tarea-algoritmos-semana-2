#Clasificando nùmeros

#Entrada de datos

num = float(input("Ingresa un numero: "))

#Uso float () para permitir datos num enteros o decimales
#input() captura el texto del usuario y float() lo convierte a número
#asimismo en este ejercicio no se hizo uso de int ya que se requiere num decimales cosa que ese code no nos permite :c

##Parte1 Validar si el num es positivo, negativo o 0

if num > 0:  #if es sí y el code/print nos mostrará el resultado de la validación en la consola / condicional 1
    print("El numero ingresado es positivo")  
    
elif num < 0:  #esto es la segunda condición (si no,si)
    print("El numero ingresado es negativo")
    
    #cuando el num no es ni mayor ni menor entonces se le considera 0 / condicional 3 (si no)
else:  #esto es la tercera condición (si no)
    print("El numero ingresado es 0")
       
##Parte2 Validar si el num es entero o decimal
if num == int(num): #Acá usamos == como comparación 
        print("El numero ingresado es un numero entero")
        
else:
        print("El numero ingresado es decimal")
        ##Caso contrario se le considera decimal