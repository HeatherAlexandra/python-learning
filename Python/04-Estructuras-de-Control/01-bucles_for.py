
#*   BUCLES FOR EN PYTHON
# Una estructura de control de bucle que itera elementos


#! 1. Bucle `for` Básico
# El uso más básico del bucle `for` es recorrer una secuencia de elementos (listas, tuplas, cadenas) y ejecutar un bloque de código en cada iteración.

# Ejemplo con una lista simple:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)  # Imprime cada número de la lista

# Explicación:
# El bucle `for` toma cada elemento de la lista `numeros` y lo asigna a la variable `numero`.
# Luego, ejecuta el bloque de código (en este caso, `print(numero)`), mostrando el valor de cada número en la lista.

# !2. Bucle `for` con `range()`
# Cuando necesitas iterar un número específico de veces, puedes usar `range()`. `range()` es muy útil para crear secuencias numéricas sin necesidad de una lista explícita.
#       !`range()`
#       tiene tres formas de uso: `range(stop)`, `range(start, stop)`       y `range(start, stop, step)`.

# Ejemplo básico de `range()`:
for i in range(5):  # Itera de 0 a 4
    print(i)

# Explicación:
# `range(5)` genera una secuencia de números desde 0 hasta 4 (sin incluir el 5), y el bucle `for` imprime cada número.
# El `range()` es ideal cuando sabes cuántas veces necesitas que se repita una acción.

# Ejemplo con `start` y `stop` (inicio y fin):
for i in range(2, 7):  # Itera de 2 a 6
    print(i)

# Ejemplo con `step` (incremento):
for i in range(0, 10, 2):  # Itera de 0 a 8, saltando de 2 en 2
    print(i)

# Explicación:
# `range(2, 7)` genera números del 2 al 6, y `range(0, 10, 2)` genera números de 0 a 8, incrementando de dos en dos.
# `range(start, stop, step)` es útil para crear secuencias de números que siguen un patrón específico.

#! 3. Bucle `for` con Condicionales
# Puedes añadir instrucciones condicionales dentro del bucle `for` para filtrar y ejecutar solo ciertos elementos que cumplan con una condición específica.
# El condicional `if` se utiliza para filtrar o cambiar el comportamiento del bucle según el valor de cada elemento.

# Ejemplo con condicionales para filtrar números pares:
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if numero % 2 == 0:  # Solo imprimimos los números pares
        print(numero)

# Explicación:
# El bucle recorre la lista `numeros`, y el `if numero % 2 == 0` verifica si el número es par.
# Si la condición se cumple, se imprime el número. Esta es una forma de filtrar los elementos durante la iteración.

# !4. Bucle `for` con Listas Anidadas
# A veces, trabajamos con listas que contienen otras listas (listas anidadas), como las matrices. En este caso, usamos bucles anidados, es decir, un bucle dentro de otro.
# El primer bucle recorre las sublistas, y el segundo recorre los elementos dentro de cada sublista.

# Ejemplo con listas anidadas (matriz):
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")  # Imprime cada número de la matriz
    print()  # Nueva línea después de cada fila

# Explicación:
# El primer bucle recorre las filas de la matriz (sublistas). El segundo bucle recorre los elementos dentro de cada fila.
# El `end=" "` en el `print()` permite que los números de la misma fila se impriman en la misma línea.
# la palabra fila y columna son palabras reservadas, son solo variables que se usan para iterar sobre la matriz.


# !  5. Bucle `for` con Diccionarios
# Los diccionarios en Python son colecciones de pares clave-valor. Puedes iterar sobre los diccionarios utilizando un bucle `for`.
# Al usar `.items()`, puedes obtener tanto las claves como los valores.

# Ejemplo con diccionario:
persona = {
    "nombre": "Juan",
    "edad": 30,
    "activo": True
}
for clave, valor in persona.items():  # .items() devuelve clave y valor
    print(f"{clave}: {valor}")

# Explicación:
# `.items()` devuelve una lista de tuplas (clave, valor) del diccionario. El bucle `for` recorre cada tupla y asigna
# la clave a `clave` y el valor a `valor`, para luego imprimirlos en el formato deseado.

# ! 6. Bucle `for` con `enumerate()`
# La función `enumerate()` devuelve tanto el índice como el valor de cada elemento de la secuencia.
# Esto es útil cuando necesitas conocer el índice del elemento mientras iteras.

# Ejemplo con `enumerate()`:
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")

# Explicación:
# `enumerate(colores)` devuelve una tupla `(índice, valor)` para cada elemento de la lista `colores`.
# Esto es útil cuando necesitas tanto el índice como el valor en una misma iteración.

# !7. Bucle `for` con `else`
# El bloque `else` en un bucle `for` se ejecuta solo si el bucle no se interrumpe mediante `break`.
# Si el bucle se interrumpe con `break`, el `else` no se ejecuta.

# Ejemplo con `else`:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        print("Encontrado el número 3.")
        break  # Sale del bucle
else:
    print("No se encontró el número 3.")  # Este bloque no se ejecuta porque el bucle se interrumpe con break

# Explicación:
# El `else` solo se ejecuta si el bucle no es interrumpido con `break`. Si el bucle termina normalmente,
# el `else` se ejecutará, pero si se encuentra un `break`, como en este caso, el `else` es ignorado.

# !8. Bucle `for` con `continue`
# La instrucción `continue` omite la iteración actual del bucle y pasa directamente a la siguiente iteración.

# Ejemplo con `continue`:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        continue  # Salta el número 3
    print(numero)

# Explicación:
# Cuando `numero == 3`, el `continue` omite el resto de la iteración actual y pasa a la siguiente. 
# Como resultado, el número 3 no se imprime.

# !9. List Comprehension
# List Comprehension es una forma concisa y eficiente de crear listas de manera compacta y expresiva.
# Esta técnica reemplaza bucles `for` largos en una sola línea de código.

# Ejemplo de List Comprehension:
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Explicación:
# `[numero for numero in numeros if numero % 2 == 0]` es una forma más compacta de escribir un bucle `for` que filtra
#el bucle que estaria reemplazando es:
# pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(pares)

#--------
# los números pares de la lista y los agrega a la lista `pares`. Es más eficiente y legible.

#! 10. Bucle `for` con Generadores
# Los generadores permiten crear iteradores eficientes que producen elementos bajo demanda. A diferencia de las listas, 
# no se generan todos los valores a la vez, lo que los hace más eficientes en memoria.

# Ejemplo con generador:
def generador():
    for i in range(5):
        yield i  # Genera los números uno por uno

for numero in generador():
    print(numero)

# Explicación:
# `yield` convierte la función en un generador, que produce un valor cada vez que es solicitado.
# En lugar de almacenar toda la secuencia, el generador devuelve un valor a la vez bajo demanda.

