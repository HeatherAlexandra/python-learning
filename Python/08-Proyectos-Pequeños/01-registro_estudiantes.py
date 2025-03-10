
# Registro de estudiantes
# Crear un programa que permita ingresar el nombre de un estudiante y su calificación.  
# El programa debe permitir ingresar la cantidad de estudiantes a registrar.

# Diccionario vacío para almacenar datos
estudiantes = {}

# Pedir cantidad de estudiantes
n = int(input("Ingrese la cantidad de estudiantes a registrar: "))
print(n)

# Pedir datos
for i in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes[nombre] = calificacion  # Guardar en el diccionario

# Mostrar resultados
print("\n  Lista de Estudiantes:")
for nombre, calificacion in estudiantes.items():
    #items() devuelve una lista de tuplas con clave y valor en cada iteracion
    print(f"  {nombre}: {calificacion}")


