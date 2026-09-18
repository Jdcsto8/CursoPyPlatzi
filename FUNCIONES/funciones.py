# funcion: es un bloque de codigo que solo se ejecuta cuando la llamamos, permite organizar y modularizar el codigo (reutilizacion)

def mi_funcion():
    print("Hola soy simon")

#mi_funcion()

def saludar(nombre): #argumentos
    print("Hola",nombre) #Parametros



#saludar("Simon")
#saludar("Bobi")

def saludo(nombre,apellido):
    print("hola como estas", nombre,apellido)

#saludo("Rumia","Lopez") 
#saludo("albeiro","Lorainz") 

def nacionalidad(nombre,nacionalidad="Colombiana"): # cuando no se coloca el argumento se puede dejar este por defecto 
    print("Hola",nombre,"de nacionalidad",nacionalidad)

#nacionalidad("john","Ucrania")
#nacionalidad("Joe")

def sumar(a,b):
    return a + b

suma = sumar(3,3)
print(suma)

def funcion():
    pass

