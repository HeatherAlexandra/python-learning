#*
#*   DATOS SIMPLES  
# Python no requiere definir explícitamente el tipo de dato, ya que los infiere automáticamente.
edad = 20       # int (entero)
precio = 19.90  # float (decimal)
nombre = "Juan" # str (cadena de texto)
activo = True   # bool (booleano)


#*   VARIABLE  
# Una variable es un identificador al que se le asigna un valor. Python permite:
# Asignacion multiple
a,b,c,d = 1,2,3,4
# Asignacion encadenada
a=b=c=1
# Reasignacion de valor
a=5
a=6
# Eliminar una variable
del a


#!DATOS COMPUESTOS  
# Python tiene 4 tipos de datos compuestos, estos almacenan multiples valores


#*   LISTAS - list
#Son colecciones ordenadas y mutables (modificables). Se definen con [].
numeros = [1, 2, 3, 4, 5]

numeros.append(6)       # Agrega un elemento al final
numeros.insert(0, 0)    # Agrega el 0 en la posición 0
numeros.extend([7, 8])  # Agrega varios elementos al final
numeros.remove(3)       # Elimina el elemento con valor 3
numeros.pop()           # Elimina el último elemento
numeros.pop(0)          # Elimina el primer elemento
numeros.clear()         # Elimina todos los elementos
numeros[0] = 100        # Modifica el primer elemento
# lo malo de las listas es que pueden consumir mas memoria al ser dinamicas



#*   TUPLAS   - tuple
#Son colecciones ordenadas pero inmutables (no se pueden modificar). Se definen con ().
coordenadas = (10, 20)
print(coordenadas[0])  # Acceder al primer elemento

#   coordenadas[0] = 30  → Esto daría un error porque las tuplas son inmutables


#*   DICCIONARIOS - dict
# Son colecciones no ordenadas de clave-valor. Se definen con {}. Las claves deben ser únicas.
persona = {
    "nombre": "Juan",
    "edad"  : 20,
    "activo": True
}

persona["nombre"] = "Pedro"     # Modificar un valor
persona["apellido"] = "Pérez"   # Agregar una nueva clave
del persona["activo"]           # Eliminar una clave
persona.clear()                 # Eliminar todos los elementos
persona = {}                    # Vaciar el diccionario


#*   CONJUNTOS - set
# Son colecciones no ordenadas de elementos únicos. Se definen con {}.
colores = {"rojo", "verde", "azul"}
colores.add("amarillo")  # Agregar un elemento
colores.remove("verde")  # Eliminar un elemento
colores.clear()  # Eliminar todos los elementos
colores = set()  # Crear un conjunto vacío

#ejemplo de conjunto
conjunto = {1,2,3,3,3,4} # {1,2,3,4} solo se almacenan valores unicos


#!METODOS UTILES PARA VARIABLES

#*  CONCATENACION DE CADENAS
# Con + (concatenacion)
nombre = "Juan"
saludo = "Hola, me llamo " + nombre
print(saludo)  # Hola, me llamo Juan

#Con f-strings (Recomendado)
#Ventaja: Más rápido y más legible.
saludo = f"Hola, me llamo {nombre}"
print(saludo)  # Hola, me llamo Juan

