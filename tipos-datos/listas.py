"""
# las listas son ordenadas
frases = ["hola","si","que tal","ahh bueno"]
# son ordenadas por cada uno va tener un indice 
print(frases[0])
print(type(frases))
# son modificables 
frases[0] = "hay como asi !!!!"
print(frases)
# premite valores duplicados 
frases = ["hola","si","que tal","ahh bueno","hola"]
print(frases)
# puede tener distintos tipos de datos
cosa = [3*8,"66+35","hola soy simon","@@"]
print(cosa)
# cantidad de elememtps en una lista
print(len(cosa))
# rango de indices 
print(cosa[0:])
print(cosa[:7])
print(cosa[0:2])
# se puede buscar si un elemento x hacer parte de una lista
if 24 in cosa:
    print("24 esta en la lista y es el resultado de una operacion ")
else:
    print("elemento no encontrado")     
"""
# tiene metodos y permite agregar elementos a traves de ellos 
letras = []
#append() agrega elementos al final de la lista 
letras.append("a")
#insert() agrega de elementos en el indice que le indiques
letras.insert(0,"T")
print(letras)

# permite remover o eliminar elementos 
#remove() solo colocas el nombre del elemento
letras.remove("T")
#pop() solo colocas el indice 
letras.pop(0)
print(letras)
# permite ordenar elementos con sort()
# lista.sort()
# reverse() ordena los elementos de manera inversa 
# lista.reverse()
# union de listas 
vocales = ["a","e","o","u"]
consonantes = ["q","r","t"]
union_lista = vocales + consonantes
print(union_lista)
# otra forma de unir listas 
vocales.extend(consonantes)
print(vocales)