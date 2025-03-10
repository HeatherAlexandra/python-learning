
#*METODOS DE DICCIONARIOS (dict) dict pq es una palabra reservada
#Los diccionarios almacenan datos en pares clave:valor
#Los diccionarios son colecciones no ordenadas
#Se accede a los elementos por la clave
#Se definen con llaves {}

#!AGREGAR Y ELIMINAR ELEMENTOS
#* dict[key] = value - Agrega un elemento al diccionario o modifica el valor de una clave existente
persona = {"nombre":"Juan","edad":20}
persona["activo"] = True    #agregar un nuevo elemento
persona["nombre"] = "Pedro" #modificar el valor de una clave existente
print(persona) #{'nombre': 'Pedro', 'edad': 20, 'activo': True}

#* update({key:value}) - Agrega o actualiza varios elementos a la vez
persona.update({"apellido":"Perez","edad":21, "pais":"Mexico"})
print(persona) #{'nombre': 'Pedro', 'edad': 21, 'activo': True, 'apellido': 'Perez', 'pais': 'Mexico'}

#* pop(key) - Elimina un elemento del diccionario
persona.pop("activo")
print(persona) #{'nombre': 'Pedro', 'edad': 21, 'apellido': 'Perez', 'pais': 'Mexico'}

#* del dict[key] - Otra forma de eliminar un elemento del diccionario
del persona["apellido"]
print(persona) #{'nombre': 'Pedro', 'edad': 21, 'pais': 'Mexico'}

#* clear() - Vacia el diccionario
persona.clear()
print(persona) #{}

#!ACCESO Y METODOS UTILES
#* keys() - Devuelve una lista con las claves del diccionario
persona = {"nombre":"Juan","edad":20}
print(persona.keys()) #dict_keys(['nombre', 'edad'])
#sale dict_keys pq es un objeto iterable, se puede convertir a lista
#o sea que se puede recorrer con un for, por ejemplo:
for clave in persona.keys():
    print(clave) #nombre edad
#o se puede convertir a lista
print(list(persona.keys())) #['nombre', 'edad'] 


#* values() - Devuelve una lista con los valores del diccionario
print(persona.values()) #dict_values(['Juan', 20])

#* items() - Devuelve una lista con los pares clave:valor
print(persona.items()) #dict_items([('nombre', 'Juan'), ('edad', 20)])

#* get(key, default value) -  Obtiene el valor de una clave sin error si no existe
print(persona.get("nombre")) #Juan
print(persona.get("apellido")) #None


#setdefault(key, default value) - Obtiene el valor de una clave sin error si no existe, la crea
print(persona.setdefault("nombre")) #Juan #puesto q ya existe lo devuelve
#y si no existe?
print(persona.setdefault("apellido")) #None #como no existe, lo crea
print(persona) #{'nombre': 'Juan', 'edad': 20, 'apellido': None}
# y si no quiero que sea none?
print(persona.setdefault("apellido","Perez")) #Perez
print(persona) #{'nombre': 'Juan', 'edad': 20, 'apellido': 'Perez'}
