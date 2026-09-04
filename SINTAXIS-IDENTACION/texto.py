print("'hola'")

ingles = " I'm Simon"
print(ingles)

multiples = """ hola
no lo puedo 
creer ! 
es 
Verdad """

print(multiples)


# como saber cuantas palabras tiene un texto con el metodo len()

palabra = "Murcielago"
print(len(palabra))

# validar si una palabra esta en un texo
texto = "Este un mensaje de la letra m, sabes quien es m , esta seguro de que vistes a m"
estaIncluida = "m" in texto
print(estaIncluida)
# validar si una palabra no esta en un texo
noEstaIncluida = "M" not in texto
print(noEstaIncluida)

# convertir a minusculas y mayusculas 
mayuscula = texto.upper()
minuscula = texto.lower()

print(mayuscula)
print(minuscula)

texto2 = "    soy Pibubuja  "
sinEspacio = texto2.strip()
print(sinEspacio)





