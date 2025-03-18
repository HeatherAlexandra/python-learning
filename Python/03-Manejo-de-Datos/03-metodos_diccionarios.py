#! MÉTODOS DE DICCIONARIOS EN PYTHON
# Los diccionarios son colecciones de pares clave-valor. 
# Cada clave en un diccionario es única y se asocia con un valor.
# A partir de Python 3.7, los diccionarios mantienen el orden de inserción de los elementos.
# Los diccionarios se definen usando llaves {}.

# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 20
}

#! AGREGAR Y ELIMINAR ELEMENTOS
#* dict[key] = value - Agrega un nuevo par clave-valor o modifica el valor de una clave existente
#        # Si la clave no existe, se agrega un nuevo par clave-valor. Si la clave existe, se actualiza su valor.
persona["activo"] = True    # Agrega un nuevo par clave-valor al diccionario
persona["nombre"] = "Pedro" # Modifica el valor asociado a la clave "nombre"
print(persona)  # {'nombre': 'Pedro', 'edad': 20, 'activo': True}

#* update({key:value}) - Agrega o actualiza varios elementos a la vez
#        # Permite pasar un diccionario con las claves y valores que se desean agregar o actualizar.
#        # Si una clave ya existe, su valor se actualiza; si no existe, se crea.
persona.update({"apellido": "Perez", "edad": 21, "pais": "Mexico"})
print(persona)  # {'nombre': 'Pedro', 'edad': 21, 'activo': True, 'apellido': 'Perez', 'pais': 'Mexico'}

#* pop(key) - Elimina un elemento del diccionario y devuelve su valor
#        # El método pop() elimina la clave especificada y devuelve su valor. Si la clave no existe, se genera un KeyError.
persona.pop("activo")
print(persona)  # {'nombre': 'Pedro', 'edad': 21, 'apellido': 'Perez', 'pais': 'Mexico'}

#* del dict[key] - Otra forma de eliminar un elemento del diccionario
#        # El operador del también elimina el par clave-valor. Si la clave no existe, se genera un KeyError.
del persona["apellido"]
print(persona)  # {'nombre': 'Pedro', 'edad': 21, 'pais': 'Mexico'}

#* clear() - Vacia el diccionario, eliminando todos los elementos
#        # El método clear() elimina todos los pares clave-valor del diccionario.
persona.clear()
print(persona)  # {}

#! ACCESO Y MÉTODOS ÚTILES
# Los diccionarios proporcionan varios métodos útiles para acceder y manipular los datos almacenados.

#* keys() - Devuelve una vista de las claves del diccionario
#        # La vista de claves es un objeto iterable que se puede convertir a lista o recorrer con un bucle.
persona = {
    "nombre": "Juan",
    "edad": 20
}
print(persona.keys())  # dict_keys(['nombre', 'edad'])
#        # Podemos convertir la vista a lista si lo deseamos:
print(list(persona.keys()))  # ['nombre', 'edad']

#* values() - Devuelve una vista de los valores del diccionario
#        # Similar a keys(), values() devuelve los valores en una vista iterable.
print(persona.values())  # dict_values(['Juan', 20])

#* items() - Devuelve una vista de los pares clave-valor del diccionario
#        # Devuelve un objeto iterable con los pares clave:valor como tuplas.
print(persona.items())  # dict_items([('nombre', 'Juan'), ('edad', 20)])

#* get(key, default value) - Obtiene el valor de una clave sin error si no existe
#        # Si la clave no existe, retorna el valor por defecto (None si no se especifica otro valor).
print(persona.get("nombre"))  # Juan
print(persona.get("apellido"))  # None

#* setdefault(key, default value) - Obtiene el valor de una clave sin error si no existe, y la crea si no existe
#        # Si la clave existe, retorna su valor. Si no existe, la agrega con el valor por defecto.
print(persona.setdefault("nombre"))  # Juan
#        # Como "apellido" no existe, setdefault() lo crea con el valor None
print(persona.setdefault("apellido"))  # None
print(persona)  # {'nombre': 'Juan', 'edad': 20, 'apellido': None}

#        # Podemos pasar un valor por defecto al usar setdefault() para no obtener None
print(persona.setdefault("apellido", "Perez"))  # Perez
print(persona)  # {'nombre': 'Juan', 'edad': 20, 'apellido': 'Perez'}
