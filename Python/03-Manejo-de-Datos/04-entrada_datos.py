# 

#*ENTRADA  DE DATOS (input())
# se puede pedir datos al usuario con la funcion input() 
# esta funcion siempre devuelve un string
nombre = input("Cual es tu nombre? ")
print(f"Hola, {nombre}") #Hola, Heather

# se puede convertir el string a otro tipo de dato
edad = int(input("Cual es tu edad? "))
print(f"Tienes {edad} años") #Tienes 20 años

#si el usuario ingresa un dato incorrecto, se puede capturar la excepcion con try except valueError
try:
    edad = int(input("Cual es tu edad? "))
    print(f"Tienes {edad} años")
except ValueError:
    print("El valor ingresado no es un numero entero")  
#para evitar que el programa se detenga
