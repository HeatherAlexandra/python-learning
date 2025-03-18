#Python usa indentación para definir bloques de código, en lugar de {} como en otros lenguajes.
#La convención es usar 4 espacios para la indentación.
#elif es una abreviatura de "else if".

#! CONDICIONALES
#Las condiciones (if-elif-else) permiten ejecutar código según se cumplan ciertas condiciones.

#ESTRUCTURA
#if condición_1:
#    # Código si condición_1 es verdadera
#elif condición_2:
#    # Código si condición_2 es verdadera
#elif condición_3:
#    # Puedes tener tantos elif como necesites
#else:
#    # Código si ninguna condición es verdadera




#?Ejemplo:
nombre = input("Cual es tu nombre? ")
try:
    

    ingreso_mensual= float(input("Cual es tu ingreso mensual? "))
    gasto_mensual=  float(input("Cual es tu gasto mensual? "))

    ahorro = ingreso_mensual - gasto_mensual

    if ingreso_mensual > 10000: #si el ingreso mensual es mayor a 10000
        #entonces se evalua :
        if  ahorro == 0: #si el ahorro es igual a 0
            print(f"{nombre}, estas sin ni un centavo")
        elif ahorro < 0: #si el ahorro es menor a 0
            print(f"{nombre}, estas en deuda")
        elif ahorro > 500: #si el ahorro es mayor a 100
            print(f"{nombre}, estas ahorrando bien")
        else: #si no se cumple ninguna de las condiciones anteriores
            print(f"{nombre}, estas ahorrando poco")

    elif ingreso_mensual > 2000: #si el ingreso mensual es mayor a 2000
        print(f"{nombre}, estas bien en peru")

    elif ingreso_mensual > 1000:
        print(f"{nombre}, estas bien en venezuela")

    else :
        print(f"Lo siento {nombre}, eres pobre")
        
except ValueError:
    print("  Error: Ingresa un valor numérico válido para los ingresos y gastos.")

