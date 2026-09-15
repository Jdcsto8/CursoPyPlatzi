# coleccion de pares clave valor (ordenadas a partir de python 3.7)

articulos  = {

    1 : "manzana",
    2 : "guayabas",
    3 : "uvas",
    4 : "fresas"

}

print(articulos)
print(articulos[1])
print(articulos.get(3))

print(articulos.keys())
print(articulos.values())


# saber si un elemento existe en el diccionario 
if 1 in articulos: # solo valida la clave 
    print("articulo existente ")
else:
    print("articulo no existe ")    

# modificaciones 
articulos[4] = "Bananos"
#print(articulos)

# agrega articulos
articulos[5] = "Sandia"
#print(articulos)
articulos.update({4:"Mamoncillo",6:"Kiwui",7:"Durazno"})
#print(articulos)

# eliminacion 
#articulos.pop(2)
#print(articulos)
#articulos.popitem() # elimina el ultimo item del diccionario
#print(articulos)
#articulos.clear() # vacia el contenido del diccionario
#print(articulos)

# recorre con un bulce el diccionario 
#for k in articulos:
    #print(k)

#for v in articulos.values():
    #print(v)   

#for k,v in articulos.items():
    #print(k,v)    

# dicionarios anidados 

familia = {
    "hijos1" : {
        "nombre":"Pedro",
        "edad": 8

    },

    "hijos2" : {
        "nombre":"Ana",
         "edad": 6

            
    },
    
    "hijos3" : {
        "nombre":"Marcelo",
        "edad": 3

            
    }







}


print(familia["hijos1"]["edad"])
