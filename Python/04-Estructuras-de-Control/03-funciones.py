
#*   FUNCIONES INTEGRADAS EN PYTHON (Built-in Functions)
# Python proporciona un conjunto de funciones integradas muy útiles que no requieren importar ninguna biblioteca adicional.
# Estas funciones están disponibles directamente en el entorno de Python y permiten realizar tareas comunes de manera sencilla.

# ! 1. `print()`
# Imprime el valor de los objetos pasados como argumento.
print("Hola, mundo!")  # Imprime "Hola, mundo!"

# Explicación:
# `print()` se utiliza para mostrar valores en la consola. Es una de las funciones más básicas y más usadas en Python.

# ! 2. `len()`
# Devuelve la longitud de un objeto (como una cadena, lista, tupla, etc.).
print(len("Python"))  # Devuelve 6
print(len([1, 2, 3, 4]))  # Devuelve 4

# Explicación:
# `len()` devuelve el número de elementos de una secuencia (cadenas, listas, tuplas, etc.). 
# Es útil cuando quieres saber cuántos elementos tiene una colección.

# ! 3. `type()`
# Devuelve el tipo de un objeto.
print(type(42))  # <class 'int'>
print(type("Hola"))  # <class 'str'>

# Explicación:
# `type()` se usa para obtener el tipo de un objeto. Esto es útil cuando necesitas verificar el tipo de una variable.

# ! 4. `int()`, `float()`, `str()`
# Convierte un valor a tipo `int`, `float` o `str` respectivamente.
print(int("42"))  # Convierte "42" a 42 (entero)
print(float("3.14"))  # Convierte "3.14" a 3.14 (decimal)
print(str(100))  # Convierte 100 a "100" (cadena de texto)

# Explicación:
# Estas funciones se utilizan para convertir entre diferentes tipos de datos (enteros, flotantes, cadenas, etc.).

# ! 5. `input()`
# Lee una línea de entrada del usuario y la devuelve como una cadena de texto.
usuario = input("¿Cómo te llamas? ")  # Solicita el nombre del usuario
print("Hola, " + usuario)

# Explicación:
# `input()` permite al programa interactuar con el usuario pidiéndole datos a través de la consola.
# Devuelve siempre una cadena de texto.

# ! 6. `sum()`
# Devuelve la suma de todos los elementos en un iterable.
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # Devuelve 15

# Explicación:
# `sum()` se utiliza para sumar todos los elementos de una secuencia como listas o tuplas. Funciona con cualquier objeto iterable.

# ! 7. `max()`, `min()`
# Devuelve el valor máximo o mínimo de una secuencia.
print(max([1, 2, 3, 4, 5]))  # Devuelve 5
print(min([1, 2, 3, 4, 5]))  # Devuelve 1

# Explicación:
# `max()` devuelve el valor más alto de un iterable, mientras que `min()` devuelve el más bajo.

# ! 8. `abs()`
# Devuelve el valor absoluto de un número.
print(abs(-42))  # Devuelve 42
print(abs(3.14))  # Devuelve 3.14

# Explicación:
# `abs()` toma un número (entero o flotante) y devuelve su valor absoluto. Esto es útil cuando no te importa el signo del número.

# ! 9. `round()`
# Redondea un número a un número específico de decimales.
print(round(3.14159, 2))  # Devuelve 3.14
print(round(3.14159))  # Devuelve 3 (sin decimales)

# Explicación:
# `round()` se usa para redondear un número flotante. Puedes especificar cuántos decimales quieres en el resultado.

# ! 10. `sorted()`
# Devuelve una nueva lista ordenada (de menor a mayor, por defecto).
print(sorted([5, 3, 8, 6]))  # Devuelve [3, 5, 6, 8]

# Explicación:
# `sorted()` devuelve una lista nueva con los elementos de un iterable ordenados. No modifica el iterable original.

# ! 11. `range()`
# Devuelve un iterable que genera una secuencia de números.
print(list(range(5)))  # Devuelve [0, 1, 2, 3, 4]

# Explicación:
# `range()` se usa para generar secuencias de números, muy útil cuando se combinan con bucles `for` para repetir una acción varias veces.

# ! 12. `all()`, `any()`
# `all()` devuelve `True` si todos los elementos de un iterable son verdaderos. `any()` devuelve `True` si al menos uno es verdadero.
print(all([True, True, False]))  # Devuelve False
print(any([True, False, False]))  # Devuelve True

# Explicación:
# `all()` verifica que todos los elementos sean verdaderos, y `any()` verifica que al menos uno sea verdadero. Son útiles para validar condiciones.


# ! 13. `enumerate()`
# Devuelve un iterable que contiene pares índice-valor de una secuencia.
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(indice, color)

# Explicación:
# `enumerate()` permite acceder tanto al índice como al valor de los elementos en un iterable, lo cual es útil cuando necesitas ambos.


# ! 14. `zip()`
# Une varios iterables (listas, tuplas) y devuelve un iterable de tuplas con los elementos correspondientes.
nombres = ["Juan", "Ana", "Pedro"]
edades = [28, 22, 30]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Explicación:
# `zip()` empareja los elementos de varios iterables, combinando sus elementos en tuplas. Es útil para iterar en paralelo sobre varias secuencias.
#  Entonces imprime:
# Juan tiene 28 años
# Ana tiene 22 años
# Pedro tiene 30 años


# ! 15. `isinstance()`
# Verifica si un objeto es una instancia de una clase o tipo específico.
print(isinstance(42, int))  # Devuelve True
print(isinstance("Hola", str))  # Devuelve True
print(isinstance([1, 2, 3], list))  # Devuelve True
# Explicación:
# `isinstance()` verifica si un objeto es una instancia de un tipo o clase dada, lo cual es útil para hacer validaciones de tipo.


# ! 16. `id()`
# Devuelve la identidad de un objeto (su dirección de memoria).
x = 10
print(id(x))  # Devuelve la dirección de memoria de 'x'
# Explicación:
# `id()` devuelve un número único que identifica el objeto en memoria. Es útil para comparar objetos o verificar la identidad en el contexto de mutabilidad.

# ! 17. `del`
# Elimina un objeto (una variable, una clave en un diccionario, un elemento de una lista, etc.).
x = 10
del x  # Elimina la variable `x`
# Explicación:
# `del` elimina un objeto de la memoria, ya sea una variable, un elemento en una lista o una clave en un diccionario. Es útil para liberar recursos.

# ! 18. `set()`
# Convierte un iterable en un conjunto (una colección de elementos únicos).
numeros = [1, 2, 2, 3, 4, 4, 5]
print(set(numeros))  # Devuelve {1, 2, 3, 4, 5}

# Explicación:
# `set()` convierte un iterable en un conjunto, eliminando los elementos duplicados. Es útil cuando necesitas trabajar con elementos únicos.

# ! 19. `dir()`
# Devuelve una lista de los atributos y métodos de un objeto.

print(dir("cadena"))  # Muestra los métodos y atributos de la cadena
#Entonces imprime:
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Explicación:
# `dir()` se utiliza para obtener la lista de todos los métodos y atributos disponibles para un objeto, útil para explorar clases o módulos.




