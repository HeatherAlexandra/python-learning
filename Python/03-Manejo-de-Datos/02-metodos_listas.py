#! MÉTODOS DE LISTAS EN PYTHON
# Las listas en Python son colecciones ordenadas y mutables, lo que significa que puedes modificar, agregar o eliminar elementos de ellas. 
# Se pueden usar para almacenar una secuencia de elementos, que pueden ser de cualquier tipo de datos (enteros, cadenas, otros objetos, etc.).

# Crear una lista
frutas = ["manzana", "banana", "cereza"]
# Las listas son creadas usando corchetes [] y los elementos dentro están separados por comas.

#! AGREGAR Y ELIMINAR ELEMENTOS
# Las listas permiten agregar o eliminar elementos de manera eficiente.

#* append() - Agrega un elemento al final de la lista
colores = ["rojo", "verde", "azul"]
colores.append("amarillo")
# La función append() agrega un solo elemento al final de la lista. 
# Este método modifica la lista original y no devuelve ningún valor (retorna 'None').
print(colores) # ['rojo', 'verde', 'azul', 'amarillo']

#* insert(posicion, valor) - Agrega un elemento en la posición indicada
lista = [1, 2, 3, 4, 5]
lista.insert(0, 0)
# La función insert() permite agregar un elemento en una posición específica dentro de la lista.
# El primer argumento es el índice donde se insertará el elemento, y el segundo es el valor que se insertará.
print(lista) # [0, 1, 2, 3, 4, 5]

#* pop(posicion) - Elimina un elemento en la posición indicada
lista.pop(0)
# El método pop() elimina y devuelve el elemento en la posición especificada. Si no se indica una posición, 
# por defecto elimina el último elemento de la lista.
print(lista) 
# [1, 2, 3, 4, 5] (El primer elemento, 0, ha sido eliminado)

#* remove(valor) - Elimina el primer elemento con el valor indicado
lista.remove(3)
# Este método elimina la primera aparición del valor especificado en la lista.
# Si el valor no se encuentra, se lanza una excepción ValueError.
print(lista) # [1, 2, 4, 5]

#* clear() - Elimina todos los elementos de la lista
lista.clear()
# El método clear() elimina todos los elementos de la lista, dejándola vacía.
print(lista) # []

#! EXTENDER LISTAS
#* extend([valores]) - Agrega varios elementos al final de la lista
lista = [1, 2, 3]
lista.extend([4, 5, 6])
# La función extend() permite agregar múltiples elementos a una lista. 
# El argumento de esta función debe ser un iterable (como una lista o una tupla).
print(lista) # [1, 2, 3, 4, 5, 6]

#! CONCATENAR LISTAS
#* El operador + puede usarse para concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
# El operador + permite concatenar dos listas, creando una nueva lista que contiene los elementos de ambas.
print(lista3) # [1, 2, 3, 4, 5, 6]

#! MODIFICAR ELEMENTOS
# Las listas en Python son mutables, lo que significa que se pueden modificar directamente.

#* Se pueden modificar los elementos de una lista directamente mediante su índice
lista = [1, 2, 3, 4, 5]
lista[0] = 100
# Los elementos de la lista se acceden mediante su índice (comenzando desde 0), y pueden ser modificados directamente.
# Aquí se cambia el primer elemento (índice 0) a 100.
print(lista) # [100, 2, 3, 4, 5]

#! ORDENAMIENTO Y BUSQUEDA
# Los métodos de ordenamiento y búsqueda permiten trabajar eficientemente con las listas.

#* sort() - Ordena la lista (ascendente por defecto)
lista = [3, 1, 2, 5, 4]
lista.sort()
# El método sort() ordena la lista en su lugar, modificando la lista original.
# Si la lista contiene números, los ordena de menor a mayor.
print(lista) # [1, 2, 3, 4, 5]

#* ¿Y si son palabras? - sort() ordena las cadenas alfabéticamente
colores = ["rojo", "verde", "azul"]
colores.sort()
# sort() también ordena cadenas de texto alfabéticamente, basándose en el orden Unicode de las letras.
# Este tipo de ordenamiento es útil para organizar palabras o frases.
print(colores) # ['azul', 'rojo', 'verde']

#* sort(reverse=True) - Ordena la lista en orden descendente
lista = [3, 1, 2, 5, 4]
lista.sort(reverse=True)
# El argumento reverse=True le dice al método sort() que ordene la lista de mayor a menor.
print(lista) # [5, 4, 3, 2, 1]

#* index(valor) - Devuelve la posición del primer elemento con el valor indicado
lista = [3, 1, 2, 5, 4]
print(lista.index(2)) # 2, ya que el valor 2 está en la posición 2

#* reverse() - Invierte el orden de la lista
lista = [3, 1, 2, 5, 4]
lista.reverse()
# El método reverse() invierte el orden de los elementos en la lista, modificando la lista original.
print(lista) # [4, 5, 2, 1, 3]

#* count(valor) - Cuenta cuántas veces aparece un valor en la lista
lista = [3, 1, 2, 5, 4, 2, 2]
print(lista.count(2)) # 3, ya que el valor 2 aparece tres veces en la lista

#* copy() - Copia una lista (evita problemas al modificar la lista original)
lista = [3, 1, 2, 5, 4]
copia = lista.copy()
# La función copy() crea una copia superficial de la lista original. 
# Esto significa que si modificamos la copia, la lista original no se ve afectada.
print(copia) # [3, 1, 2, 5, 4]
