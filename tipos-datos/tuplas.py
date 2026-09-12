# son inmutables 
letras = ("a","b","c")

print(letras)
print(letras[2])
print(len(letras))
# puede tener distintos tipos de datos
# para tener crear un tupla de un solo elementos debe siempre colocarlse un coma ,
cosas = ("asi",)
print(type(cosas))

# desempaquetar tuplas 

tupla = ("q","w","r")
x,y,z = tupla
print(x)
print(y)
print(z)

# union de tuplas , tambine puede tener elementos duplicados
tupla2 = ("h","p","p")
tupla3 = tupla + tupla2

# se puede duplicar las tuplas 
print(tupla3 * 2)
# se puede recorrer con un bucle for 
for item in tupla3:
    print(item)


# como las tuplas son inmutables se pueden manipular conviertodalas en listas y luego volverla a tuplas 
listaComodin= list(tupla3)  
print(listaComodin)  
listaComodin.append("z")
listaComodin.append("i")
listaComodin.append("o")
print(listaComodin)
tupla3 = tuple(listaComodin)
print(tupla3)