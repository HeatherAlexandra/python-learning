
#! Desempaquetado de datos	
# Se puede dar para listas, tuplas, conjuntos y diccionarios

#creando los datos
datos_en_tupla = ("Heather","Valencia", 1000 ) # tupla
datos_en_lista = ["Heather","Valencia", 1000 ] # lista
datos_en_conjunto = {"Heather","Valencia", 1000 } # conjunto
datos_en_diccionario = {"nombre":"Heather","apellido":"Valencia", "edad":1000 } # diccionario

#desempaquetando los datos
nombre, apellido, edad = datos_en_tupla
print(nombre)
print(apellido)
print(edad)

