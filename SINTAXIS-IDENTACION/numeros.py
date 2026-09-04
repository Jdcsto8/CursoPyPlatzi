x = 1 
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

positivo = 5
negativo = -5.5
imaginario = 5 + 1j 
imaginarioNegativo = -5 -1j


# casteo

xf = float(x)
print(type(xf))

ye = int(y)
print(type(ye))
print(ye)

# se puede castear integer y float a complejo pero no al contrario 

enteroComplejo = complex(positivo)
flotanteComplejo = complex(negativo)

print(enteroComplejo)
print(type(enteroComplejo))
print(flotanteComplejo)
print(type(flotanteComplejo))

# numeros aleatorios 


import random

print(random.randrange(1,10))
