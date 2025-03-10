

#? Formateo de cadenas con f-strings
#siempre se escribe anteponiendo f o F 
# antes de las comillas ("" o ''):
#Las f-strings (f"") permiten insertar valores dentro de un string
# ejemplo
nombre = "Juan"
edad = 20
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
#Salida: Hola, me llamo Juan y tengo 20 años.
#siempre se debe anteponer una f al inicio de las comillas dobles o simples
#dentro de las llaves se pueden realizar operaciones
print(f"El doble de mi edad es {edad*2}")
#Salida: El doble de mi edad es 40
#se pueden usar funciones
print(f"Mi nombre en mayusculas es {nombre.upper()}")
#Salida: Mi nombre en mayusculas es JUAN
#se pueden usar expresiones
print(f"El resultado de la suma es {10+5}")
#Salida: El resultado de la suma es 15
#se pueden usar diccionarios
persona = {"nombre":"Juan","edad":20}
print(f"Mi nombre es {persona['nombre']} y tengo {persona['edad']} años.")
#Salida: Mi nombre es Juan y tengo 20 años.
#se pueder formatear numeros
numero = 10/3
print(f"El resultado de la division es {numero:.2f}") #FLOAT
#Salida: El resultado de la division es 3.33
# la f al inicio de las comillas indica que es una f-string
# la f al final de la llave indica que se va a formatear el valor
# el : indica que se va a formatear
# el .2f indica que se va a formatear a dos decimales
 
print(f"El resultado de la division es {numero:.2%}")
#Salida: El resultado de la division es 333.33%
# el % indica que se va a formatear a porcentaje
 
print(f"El resultado de la division es {numero:.2e}")
#Salida: El resultado de la division es 3.33e+00
# el e indica que se va a formatear a notacion cientifica

print(f"El resultado de la division es {numero:.2g}")
#Salida: El resultado de la division es 3.3
# el g indica que se va a formatear a notacion general

# o para alinear textos
nombre = "Juan"
edad = 20
print(f"{nombre:<10} | {edad:>10}")
#Salida: Juan       |         20
# el < indica que se va a alinear a la izquierda
# el 10 indica el ancho del texto
# el > indica que se va a alinear a la derecha
# si quieres centrar el texto se usa ^
print(f"{nombre:^10} | {edad:^10}")
#Salida:   Juan    |     20
# el ^ indica que se va a centrar el texto


#*  METODOS DE CADENAS o STRINGS
# los strings son inmutables, no se pueden modificar

#*Manipulacion de texto
    # se pueden manipular los textos con metodos
    # lower() convierte el texto a minusculas
    # upper() convierte el texto a mayusculas
texto = "Hola Mundo"
print(texto.lower()) # hola mundo
print(texto.upper()) # HOLA MUNDO

    # capitalize() convierte la primera letra en mayuscula
    # title() convierte la primera letra de cada palabra en mayuscula
print(texto.capitalize()) # Hola mundo
print(texto.title()) # Hola Mundo

    # swapcase() convierte las mayusculas en minusculas y viceversa
print(texto.swapcase()) # hOLA mUNDO

    # replace() reemplaza un texto por otro
print(texto.replace("Mundo","Amigo")) # Hola Amigo

    # strip() elimina los espacios al inicio y al final
    # lstrip() elimina los espacios al inicio
    # rstrip() elimina los espacios al final
texto = "    Te amo Heather   "
print(texto.strip()) # "Te amo Heather"
print(texto.lstrip()) # "Te amo Heather   "
print(texto.rstrip()) # "    Te amo Heather"

    # split() convierte el texto en una lista
texto = "manzana,pera,naranja"# se puede especificar el separador O COMA
print(texto.split(",")) # ['manzana', 'pera', 'naranja']
texto = "manzana pera naranja" # si no se especifica el separador se usa el espacio
print(texto.split()) # ['manzana', 'pera', 'naranja'] 

    # join() convierte una lista en un texto
frutas = ["manzana","pera","naranja"]
print(",".join(frutas)) # manzana,pera,naranja
print(" ".join(frutas)) # manzana pera naranja
print("".join(frutas)) # manzanaperanaranja

    # find() busca un texto en otro e index tiene la misma funcion
cadena = "Hola dios"
subcadena = "Mundo"
print(cadena.find(subcadena)) #? -1 ya que no se encuentra
subcadena = "dios"
print(cadena.find(subcadena)) #? 5 ya que se encuentra en la posicion 5
# que es posicion 5? Es la posicion donde comienza la subcadena

    # count() cuenta cuantas veces aparece un texto
cadena = "Hola mundo, hola dios, hola bombona, hola chiquita"
subcadena = "hola"
print(cadena.count(subcadena)) # 4 ya que aparece 4 veces

    # startswith() verifica si el texto comienza con otro
    # endswith() verifica si el texto termina con otro
cadena = "Hola mundo"
subcadena = "Hola"
print(cadena.startswith(subcadena)) # True
print(cadena.endswith(subcadena)) # False
