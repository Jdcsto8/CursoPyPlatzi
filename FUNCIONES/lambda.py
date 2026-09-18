# Lambda es una funcion pequeña y anonima que puede tener muchos argumentos pero solo una expresion
# Sintaxis labmda argumentos : expresion

x = lambda a: a + 15
#print(x(15))

x = lambda a,b: a + b
print(x(50,50))

# fabrica de funciones

def mifuncion(n):
    return lambda a: a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5))
print(triplicador(5))



