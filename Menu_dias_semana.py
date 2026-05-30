entrada = int(input("Ingresa un número del 1 al 7: "))

match entrada:
    #utilizamos match-case para determinar el dia de la semana segun el numero ingresado por el usuario
    case 1:
        #si el numero es 1, se retorna "Lunes"
        print("Lunes")
    case 2:
        #si el numero es 2, se retorna "Martes"
        print("Martes")
    case 3:
        #si el numero es 3, se retorna "Miércoles"
        print("Miércoles")
    case 4:
        #si el numero es 4, se retorna "Jueves"
        print("Jueves")
    case 5:
        #si el numero es 5, se retorna "Viernes"
        print("Viernes")
    case 6:
        #si el numero es 6, se retorna "Sábado"
        print("Sábado")
    case 7:
        #si el numero es 7, se retorna "Domingo"
        print("Domingo")
        #si usuario ingresa un numero fuera del rango 1-7, se muestra un mensaje de error
    case _:
        print("Número no válido. Por favor, ingresa un número del 1 al 7.")
    