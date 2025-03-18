

#! ENTRADA DE DATOS EN PYTHON
# En Python, podemos obtener datos de entrada del usuario utilizando la función input().
# Los datos introducidos por el usuario son siempre de tipo cadena (string), 
# por lo que debemos realizar conversiones si se necesitan otros tipos de datos, como enteros o flotantes.

#* input() - Lee una línea de entrada de texto desde el usuario
#        # Esta función muestra un mensaje (opcional) y espera a que el usuario ingrese algo en el teclado.
#        # El valor devuelto siempre es una cadena de texto.
nombre = input("¿Cuál es tu nombre? ")  # Solicita al usuario su nombre
print(f"Hola, {nombre}!")  # Imprime el saludo con el nombre ingresado

#* Conversión de tipos de datos - Si necesitas convertir la entrada de texto a otro tipo (como entero o flotante), puedes usar las funciones int() o float().
edad = input("¿Cuántos años tienes? ")  # Lee la edad como texto
#        # Convertimos la edad de texto a un número entero usando int()
edad = int(edad)  # Convierte la entrada a un número entero
print(f"Tienes {edad} años.")  # Imprime la edad con el valor convertido

#* Manejo de entradas numéricas con float() - Si necesitamos trabajar con decimales, podemos usar float()
precio = input("¿Cuál es el precio del producto? ")  # Lee el precio como texto
#        # Convertimos el precio de texto a un número flotante usando float()
precio = float(precio)  # Convierte la entrada a un número flotante
print(f"El precio del producto es {precio} dólares.")  # Imprime el precio con el valor convertido

#* Manejo de entradas con try-except - Usamos try-except para manejar posibles errores si la conversión falla
try:
    cantidad = input("¿Cuántos productos deseas comprar? ")
    cantidad = int(cantidad)  # Intentamos convertir la entrada a entero
    print(f"Vas a comprar {cantidad} productos.")
except ValueError:
    #        # Si ocurre un error (por ejemplo, si el usuario ingresa texto en lugar de un número),
    #        # se maneja el error y se imprime un mensaje amigable.
    print("Por favor, ingresa un número válido.")

#* input() con validación - Asegurarse de que el usuario ingrese un valor correcto
#        # Podemos utilizar un ciclo while para asegurarnos de que la entrada sea válida
while True:
    edad_usuario = input("Ingresa tu edad (solo números): ")
    if edad_usuario.isdigit():  # Verifica si la entrada solo contiene dígitos
        edad_usuario = int(edad_usuario)  # Convierte la entrada a entero
        print(f"Tu edad es {edad_usuario}.")
        break  # Sale del ciclo cuando la entrada es válida
    else:
        print("Por favor, ingresa un valor numérico válido.")

