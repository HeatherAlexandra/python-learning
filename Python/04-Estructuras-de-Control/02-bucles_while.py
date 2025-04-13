
#*   BUCLE WHILE EN PYTHON

# El bucle `while` en Python es una estructura de control que repite un bloque de código mientras una condición sea verdadera.
# Es muy útil cuando no sabes de antemano cuántas veces debes ejecutar el bloque de código, sino que depende de una condición que se evalúa en cada iteración.

# !1. Bucle `while` Básico
# El bucle `while` ejecuta el bloque de código mientras la condición sea verdadera. Si la condición es falsa desde el inicio, el bucle no se ejecuta.

# Ejemplo simple de `while`: 
contador = 0
while contador < 5:  # Mientras contador sea menor que 5
    print(contador)   # Imprime el valor de contador
    contador += 1     # Incrementa contador en 1

# Explicación:
# El bucle `while` verifica la condición `contador < 5`. Si es verdadera, ejecuta el bloque de código.
# En cada iteración, se incrementa `contador` en 1 hasta que la condición se vuelva falsa (cuando `contador` llegue a 5).

# !2. Bucle `while` con Condicionales
# Dentro del bucle `while`, se pueden usar condicionales `if` para controlar el flujo de ejecución, permitiendo hacer cosas específicas solo cuando se cumpla una condición.

# Ejemplo con `if` dentro de `while`:
contador = 0
while contador < 10:
    if contador % 2 == 0:  # Solo imprime los números pares
        print(contador)
    contador += 1

# Explicación:
# El bucle `while` sigue iterando mientras `contador` sea menor que 10.
# Dentro del bucle, se verifica si `contador` es par (`if contador % 2 == 0`) y, si es así, se imprime.

# ! 3. Bucle `while` con `break`
# La instrucción `break` permite salir de un bucle `while` antes de que la condición se vuelva falsa.
# Esto es útil cuando se cumple una condición especial dentro del bucle y deseas interrumpir la ejecución.

# Ejemplo con `break`:
contador = 0
while True:  # Esto crea un bucle infinito
    if contador == 5:
        break  # Sale del bucle cuando contador llega a 5
    print(contador)
    contador += 1

# Explicación:
# La condición del `while` es `True`, lo que significa que el bucle es infinito.
# Sin embargo, cuando `contador` llega a 5, el `break` interrumpe el bucle.

#! 4. Bucle `while` con `continue`
# La instrucción `continue` omite la iteración actual del bucle y pasa directamente a la siguiente.
# Esto es útil cuando quieres saltarte ciertas iteraciones sin salir del bucle.

# Ejemplo con `continue`:
contador = 0
while contador < 10:
    contador += 1
    if contador == 3:
        continue  # Salta la iteración cuando contador es 3
    print(contador)

# Explicación:
# El `continue` hace que el bucle pase inmediatamente a la siguiente iteración cuando `contador` es igual a 3.
# Como resultado, el número 3 no se imprime.

# !5. Bucle `while` con `else`
# Al igual que en el bucle `for`, el bucle `while` puede tener un bloque `else` que se ejecuta si el bucle termina normalmente (sin un `break`).

# Ejemplo con `else`:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle terminó correctamente.")

# Explicación:
# El bloque `else` se ejecuta cuando el bucle termina de forma natural (sin que se interrumpa con un `break`).
# En este caso, el mensaje "El bucle terminó correctamente." se imprimirá después de que el bucle haya recorrido todos los números.

# !6. Bucle `while` con Condición Compleja
# A veces, es útil tener condiciones más complejas en el `while`, como combinar múltiples condiciones con operadores lógicos (AND, OR).

# Ejemplo con condición compuesta:
contador = 0
while contador < 5 and contador != 3:  # La condición será verdadera hasta que contador sea 3 o llegue a 5
    print(contador)
    contador += 1

# Explicación:
# El bucle sigue ejecutándose mientras `contador` sea menor que 5 y diferente de 3.
# En cuanto `contador` llegue a 3, la condición se vuelve falsa y el bucle termina.

# !7. Bucle `while` con Contador Descendente
# El bucle `while` también se puede usar para contar de manera descendente.

# Ejemplo con contador descendente:
contador = 10
while contador > 0:
    print(contador)
    contador -= 1  # Decrementa el contador en 1

# Explicación:
# El bucle `while` se ejecuta mientras `contador` sea mayor que 0. En cada iteración, el valor de `contador` se decrementa.
# Este tipo de bucles es útil cuando necesitas realizar una acción repetida hasta alcanzar un valor mínimo.

# !8. Bucle `while` con Entrada del Usuario
# Los bucles `while` son útiles cuando necesitas realizar repeticiones basadas en la entrada del usuario.
# Por ejemplo, puedes pedirle al usuario que ingrese un número, y continuar pidiendo hasta que ingrese un valor válido.

# Ejemplo con entrada del usuario:
while True: #bucle infinito
    numero = input("Ingresa un número (o 'salir' para terminar): ")
    if numero == "salir":
        break
    print(f"Has ingresado: {numero}")

# Explicación:
# El bucle sigue ejecutándose hasta que el usuario escribe "salir". En cada iteración, se pide un número al usuario y se imprime.
# Si el usuario ingresa "salir", el `break` detiene el bucle.

# !9. Bucle `while` con Funciones y Recursión
# El bucle `while` puede interactuar con funciones y ser utilizado de manera recursiva, aunque es más común en recursión tener un caso base para evitar infinitos.

# Ejemplo con función:
def contar_hasta_5():
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

contar_hasta_5()

# Explicación:
# La función `contar_hasta_5()` contiene un bucle `while` que imprime los números del 0 al 4.
# Se puede llamar a esta función varias veces o incluirla en un programa más complejo.

#! 10. Bucle `while` con Tiempos y Esperas
# El bucle `while` también es útil para esperar ciertos eventos o tiempos de manera eficiente sin bloquear completamente el flujo de ejecución.

# Ejemplo con tiempo:
import time

contador = 0
while contador < 5:
    print(contador)
    time.sleep(1)  # Pausa el programa por 1 segundo
    contador += 1

# Explicación:
# El bucle imprime el contador y luego hace una pausa de 1 segundo antes de continuar con la siguiente iteración.
# Esto puede ser útil para ejecutar tareas en intervalos regulares.



