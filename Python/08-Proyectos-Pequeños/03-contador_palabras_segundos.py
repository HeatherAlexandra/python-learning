
# a) Pedir al usuario ingresar cualquier texto real y 
#        - calcular cuanto tardaria en escribir esa frase
#        - contar cuantas palabras tiene la frase
frase= input("Ingresa una frase y te calculo cuanto tardarias en escribirla :) : ")
palabras = frase.split() # Separa las palabras de la frase
tiempo = len(frase) / 5 # Calcula el tiempo en segundos que tardarias en escribir la frase
# por que 5? por que en promedio se escribe 5 caracteres por segundo
print(f"Tardarias {tiempo} segundos en escribir la frase")
print(f"La frase tiene {len(palabras)} palabras")

# b) Si se tarda mas de un minuto en escribir la frase, 
#    mostrar un mensaje que diga "Te dije frase mi bro, no un testamento"

if tiempo > 50:
    print("Te dije frase mi bro, no un testamento")
else:
    print("Buena frase")


#c) 