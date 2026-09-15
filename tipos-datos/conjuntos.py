# cojuntos (set) : Coleccion no ordenada de elementos unicos (no se puede acceder por indice y no reconoce elementos duplicas)

conj1 = {"gordo frio",(3**3)/3,"@_@","a","a"}

#print(type(conj1))
#print(conj1)
#print(len(conj1))

#for item in conj1:
    #print(item)
# buscar elementos 
#print(9 in conj1)  
#print("@" not in conj1)  

#agregar elementos
conj1.add(8**2)
#print(conj1)
#Update se puede agregar mas elementos , listas, tuplas 
cuadrados = {2**3,2**6,2**2-2*(2)*(3)-2**2}
conj1.update(cuadrados)
#print(conj1)

# metodos de eliminacion
# remove : si elemento a eliminar no existe genera un error
conj1.remove(-12)
#print(conj1)
#Discard : si elemento a eliminar no existe omite el error
conj1.discard(64)
#print(conj1)
# pop : elimina un elemento de manera aleatoria
conj1.pop()
#print(conj1)
#clear : borra todo el conjunto
conj1.clear()
#print(conj1)

# OPERACIONES ENTRE CONJUNTOS 

a = {1,2,3}
b = {3,4,5,6,7}

c = a.union(b)
print(c)
i = a.intersection(b)
print(i)
d = a.difference(b)
print(d)

