
#

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

#*   UNION
# Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos.
print(f"Union: {conjunto1.union(conjunto2)}")  # {1, 2, 3, 4, 5, 6, 7}
print(f"Union: {conjunto1 | conjunto2}")  # {1, 2, 3, 4, 5, 6, 7}

#*   INTERSECCION
print(f"Intersección: {conjunto1.intersection(conjunto2)}")  # {3, 4, 5}
print(f"Intersección: {conjunto1 & conjunto2}")  # {3, 4, 5}

#*   DIFERENCIA
print(f"Diferencia: {conjunto1.difference(conjunto2)}")  # {1, 2}
print(f"Diferencia: {conjunto1 - conjunto2}")  # {1, 2}

