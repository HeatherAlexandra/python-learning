
#*METODOS DE LISTAS
#Las listas son estructuras dinamicas y modificables

#!AGREGAR Y ELIMINAR ELEMENTOS

#*append() - Agrega un elemento al final de la lista
colores = ["rojo","verde","azul"]
colores.append("amarillo")
print(colores) #['rojo', 'verde', 'azul', 'amarillo']

#*insert(posicion, valor) - Agrega un elemento en la posicion indicada
lista = [1,2,3,4,5]
lista.insert(0,0)
print(lista) #[0, 1, 2, 3, 4, 5]

#*pop(posicion) - Elimina un elemento en la posicion indicada
lista.pop(0)
print(lista) #[1, 2, 3, 4, 5]

#*remove(valor) - Elimina el primer elemento con el valor indicado
lista.remove(3)
print(lista) #[1, 2, 4, 5]

#*clear() - Elimina todos los elementos de la lista
lista.clear()
print(lista) #[]

#*EXTENDER LISTAS
#*extend([valores]) - Agrega varios elementos al final de la lista
lista = [1,2,3]
lista.extend([4,5,6])
print(lista) #[1, 2, 3, 4, 5, 6]

#*CONCATENAR LISTAS
#Se pueden concatenar listas con el operador +
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3) #[1, 2, 3, 4, 5, 6]

#*MODIFICAR ELEMENTOS
#Se pueden modificar los elementos de una lista
lista = [1,2,3,4,5]
lista[0] = 100
print(lista) #[100, 2, 3, 4, 5]

#!ORDENAMIENTO Y BUSQUEDA

#*sort() - Ordena la lista (ascendente por defecto)
lista = [3,1,2,5,4]
lista.sort()
print(lista) #[1, 2, 3, 4, 5] lo ordena de menor a mayor
# y si son palabras? 
colores = ["rojo","verde","azul"]
colores.sort()
print(colores) #['azul', 'rojo', 'verde'] lo ordena alfababeticamente

#*sort(reverse=True) - Ordena la lista en orden descendente
lista = [3,1,2,5,4]
lista.sort(reverse=True)
print(lista) #[5, 4, 3, 2, 1]

#*index(valor) - Devuelve la posicion del primer elemento con el valor indicado
lista = [3,1,2,5,4]
print(lista.index(2)) #2 ya que esta en la posicion 2

#*reverse() - Invierte el orden de la lista
lista = [3,1,2,5,4]
lista.reverse()
print(lista) #[4, 5, 2, 1, 3]

#*count(valor) - Cuenta cuantas veces aparece un valor en la lista
lista = [3,1,2,5,4,2,2]
print(lista.count(2)) #3 ya que aparece 3 veces

#*copy() - Copia una lista
lista = [3,1,2,5,4]
copia = lista.copy()
print(copia) #[3, 1, 2, 5, 4]
