
#! METODOS DE CADENAS o STRINGS
# Funciones aplicadas a objetos de tipo string
# Pero que es un objeto? Un objeto es una instancia de una clase
# y una clase es un molde para crear objetos
# en python todo es un objeto, las variables, las funciones, los modulos, etc


# *ESTRUCTURA
# nombredelafuncion(parametros)


#! METODOS BASICOS DE CADENAS
#*print() - Imprime un mensaje en la consola
print("Hola Heather hermosa")

# Convierte todo el texto a mayúsculas
texto = "hola mundo"
print(texto.upper())  # HOLA MUNDO

# Convierte todo el texto a minúsculas
print(texto.lower())  # hola mundo

# Convierte la primera letra a mayúscula
print(texto.capitalize())  # Hola mundo

# Convierte la primera letra de cada palabra a mayúscula
print(texto.title())  # Hola Mundo

# Cambia las mayúsculas a minúsculas y viceversa
print(texto.swapcase())  # HOLA MUNDO

# Reemplaza una subcadena por otra
print(texto.replace("mundo", "amigo"))  # hola amigo

#!METDOS DE MANIPULACION DE ESPACIOS
# Elimina los espacios en ambos extremos de la cadena
texto = "   Hola Mundo   "
print(texto.strip())  # Hola Mundo

# Elimina los espacios a la izquierda de la cadena
print(texto.lstrip())  # Hola Mundo   

# Elimina los espacios a la derecha de la cadena
print(texto.rstrip())  #    Hola Mundo

#!METODOS DE BUSCA Y POSICIONAMIENTO
# Encuentra la primera aparición de una subcadena y devuelve su índice
cadena = "Hola Mundo"
subcadena = "Mundo"
print(cadena.find(subcadena))  # 5 (La posición donde empieza 'Mundo')

# Si la subcadena no se encuentra, devuelve -1
subcadena = "Python"
print(cadena.find(subcadena))  # -1 (No se encuentra)

# Devuelve el índice de la subcadena, pero lanza un error si no se encuentra
print(cadena.index(subcadena))  # Lanza un error, porque "Python" no existe
# Si la subcadena si existe seria asi
subcadena = "Mundo"
print(cadena.index(subcadena))  # 5 (La posición donde empieza 'Mundo')
#INDEX Y FIND devuelven la misma informacion, pero index lanza un error si no encuentra la subcadena

# Cuenta cuántas veces aparece una subcadena en la cadena
print(cadena.count("o"))  # 2 (La letra 'o' aparece dos veces)

# Verifica si la cadena comienza con la subcadena indicada
print(cadena.startswith("Hola"))  # True

# Verifica si la cadena termina con la subcadena indicada
print(cadena.endswith("Mundo"))  # True

#!METODOS DE SEPARACION Y UNION
# Divide una cadena en una lista usando un separador
texto = "manzana,pera,naranja"
print(texto.split(","))  # ['manzana', 'pera', 'naranja']

# Si no se especifica un separador, se divide por los espacios
texto = "manzana pera naranja"
print(texto.split())  # ['manzana', 'pera', 'naranja']

# Une una lista de cadenas en una sola cadena usando un separador
frutas = ["manzana", "pera", "naranja"]
print(",".join(frutas))  # manzana,pera,naranja
print(" ".join(frutas))  # manzana pera naranja
print("".join(frutas))   # manzanaperanaranja

#! METODOS DE VERIFICACION
# Verifica si todos los caracteres en la cadena son numéricos
texto = "12345"
print(texto.isnumeric())  # True

# Verifica si todos los caracteres en la cadena son alfabéticos
texto = "Hola"
print(texto.isalpha())  # True

# Verifica si la cadena tiene caracteres alfabéticos y numéricos
texto = "Hola123"
print(texto.isalnum())  # True

# Verifica si la cadena contiene solo letras mayúsculas
texto = "HOLA"
print(texto.isupper())  # True

# Verifica si la cadena contiene solo letras minúsculas
texto = "hola"
print(texto.islower())  # True

# Verifica si la cadena es un espacio vacío
texto = "   "
print(texto.isspace())  # True



#! METODOS DE FORMATEO DE CADENAS
# Los f-strings son la mejor forma de concatenar strings
# se pueden usar con comillas simples o dobles
nombre ='Heaather'
edad = 21
print(f'Hola, me llamo{nombre} y mi edad es{edad} años')
#Salida: Hola, me llamo Heather y mi edad es 21 años

#    #*Se pueden usar:
#    #? - Operaciones Matematicas:
print(f'El doble de mi edad es {edad*2}')

#    #? - Metodos de cadenas:
print(f'Mi nombre en mayusculas es {nombre.upper()}')

#    #? - Dicts o diccionarios:
persona = {'nombre':'Heather','edad':21}
print(f'Mi nombre es {persona['nombre']} y tengo {persona['edad']} años')

#    #? - Formateo de numeros:
numero = 10/3
#        #*Formato a decimales
print(f'El resultado de la division del numero es{numero:.2f}')
#        Salida: El resultado de la division del numero es 3.33
#        se pone : + . + el numero de decimales que se quiere + f
#        #*Formato a porcentaje	
print(f"El porcentaje es {numero:.2%}") 
#        Salida: El porcentaje es 333.33%
#        #*Formato a notacion cientifica
print(f"El resultado de la division es {numero:.3e}")
#        Salida: El resultado de la division es 3.333e+00
print(f"El resultado de la division es {numero:.1e}")
#        Salida: El resultado de la division es 3.3e+00
#        










