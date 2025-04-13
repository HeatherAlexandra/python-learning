# 01-archivos_txt.py
#*   MANEJO DE ARCHIVOS EN PYTHON
# El manejo de archivos es una de las tareas más comunes en programación. En Python, trabajar con archivos es sencillo gracias a las funciones integradas.

# 1. Abrir un archivo
# Para abrir un archivo en Python, se utiliza la función `open()`, que acepta el nombre del archivo y el modo de apertura.

# Ejemplo:
# 'r' - Modo de lectura (por defecto, solo lee el archivo)
# 'w' - Modo de escritura (crea un archivo nuevo o sobrescribe uno existente)
# 'a' - Modo de anexado (añade al final del archivo)
# 'x' - Modo de creación exclusiva (si el archivo existe, da error)

# Abrir un archivo en modo lectura ('r')
archivo = open("ejemplo.txt", "r")  # Abre el archivo "ejemplo.txt" en modo lectura
contenido = archivo.read()  # Lee todo el contenido del archivo
print(contenido)  # Imprime el contenido
archivo.close()  # Es importante cerrar el archivo después de usarlo

# Explicación:
# `open()` se usa para abrir un archivo, y `read()` lee todo su contenido. Es importante cerrar el archivo después de usarlo con `close()` para liberar recursos.

# 2. Leer un archivo línea por línea
# Si prefieres leer el archivo línea por línea, puedes usar `readline()` o `readlines()`.
# `readline()` lee una línea, mientras que `readlines()` lee todas las líneas y las devuelve como una lista.

# Leer archivo línea por línea:
archivo = open("ejemplo.txt", "r")
linea = archivo.readline()  # Lee la primera línea
while linea:  # Mientras haya líneas
    print(linea.strip())  # .strip() elimina saltos de línea extra
    linea = archivo.readline()  # Lee la siguiente línea
archivo.close()

# Explicación:
# `readline()` lee línea por línea. Usamos un ciclo `while` para continuar leyendo hasta que no haya más líneas en el archivo.
# `strip()` se usa para eliminar los saltos de línea.

# 3. Escribir en un archivo
# Si quieres escribir en un archivo, puedes abrirlo en modo escritura ('w') o anexado ('a').

# Abrir archivo en modo escritura ('w'), sobrescribe el archivo si ya existe
archivo = open("nuevo_archivo.txt", "w")
archivo.write("Este es el primer contenido en el archivo.\n")
archivo.write("Añadimos más líneas.\n")
archivo.close()  # No olvides cerrar el archivo

# Explicación:
# El archivo se abre en modo escritura con `'w'`. Si el archivo no existe, Python lo crea. Si existe, lo sobrescribe completamente.

# 4. Añadir contenido a un archivo existente
# Si no quieres sobrescribir el archivo, sino añadir al final de su contenido, abre el archivo en modo anexado ('a').

# Abrir archivo en modo anexado ('a')
archivo = open("nuevo_archivo.txt", "a")
archivo.write("Este es un contenido adicional.\n")
archivo.write("Más contenido en la misma línea.\n")
archivo.close()

# Explicación:
# Al abrir el archivo en modo anexado, los datos se añaden al final del archivo sin borrar el contenido existente.

# 5. Usando la instrucción `with` para manejar archivos
# El uso de la instrucción `with` es la forma recomendada de trabajar con archivos en Python. Asegura que el archivo se cierre automáticamente después de usarse, incluso si ocurre un error.

# Usar `with` para leer el archivo:
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el contenido
    print(contenido)

# Usar `with` para escribir en el archivo:
with open("nuevo_archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo creado con la instrucción `with`.\n")
    archivo.write("Es mucho más seguro y eficiente.\n")

# Explicación:
# Al usar `with`, Python maneja automáticamente el cierre del archivo, incluso si se produce una excepción en medio del bloque.

# 6. Verificar si un archivo existe antes de abrirlo
# A veces es útil verificar si un archivo existe antes de intentar abrirlo. Esto puede evitar errores al intentar abrir un archivo que no existe.

import os

# Verificar si un archivo existe antes de abrirlo
if os.path.exists("ejemplo.txt"):
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe.")

# Explicación:
# Usamos `os.path.exists()` para verificar si el archivo existe antes de intentar abrirlo, lo cual ayuda a evitar errores de "archivo no encontrado".

# 7. Manejo de excepciones al trabajar con archivos
# Es importante manejar las excepciones para asegurarse de que el programa no se detenga abruptamente si algo sale mal (como un archivo que no se puede abrir).

try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no fue encontrado.")
except IOError:
    print("Hubo un error al intentar leer el archivo.")
finally:
    if 'archivo' in locals():
        archivo.close()  # Cerramos el archivo si fue abierto

# Explicación:
# Utilizamos `try-except` para manejar errores comunes al trabajar con archivos, como si el archivo no se encuentra (`FileNotFoundError`) o hay problemas con la lectura (`IOError`).
# El bloque `finally` asegura que el archivo se cierre si fue abierto correctamente.

# 8. Eliminar un archivo
# Si necesitas eliminar un archivo, puedes usar la función `os.remove()`.

import os

# Eliminar un archivo si existe
if os.path.exists("nuevo_archivo.txt"):
    os.remove("nuevo_archivo.txt")
    print("El archivo ha sido eliminado.")
else:
    print("El archivo no existe.")

# Explicación:
# `os.remove()` elimina un archivo. Es importante verificar primero si el archivo existe para evitar errores.


