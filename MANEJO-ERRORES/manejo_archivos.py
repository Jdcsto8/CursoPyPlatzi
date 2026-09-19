# R (read) Lectura
# W (write) Escritura
# X (crea archivo nuevo)

print("hola soy Pi")
x = 3
z = 2

"""
try:
    f = open("archivo.txt","r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")    

resultado = (x+z)**3
print(resultado)
"""
# with nos permite abrir y cerrar los archivos con menos lineas de codigo

try:
    with  open("archivo.txt","r") as f:
        print(f.readline())
        print(f.readline())
    
except FileNotFoundError:
    print("No se ha encontrado el archivo")    

resultado = (x+z)**3
print(resultado)

"""
# VAMOS A ESCRIBIR EN UN AERCHIVO OJO CUANDO USAMOS WRITE SE SOBREESCRIBE EL ARCHIVO 
try:
    with  open("archivo.txt","w") as f:
          f.write("hola soy BuBuJa te he sobreescrito")
    with  open("archivo.txt","r") as f:
            print(f.readline())   
  
except FileNotFoundError:
    print("No se ha encontrado el archivo")

"""

"""
# VAMOS A ESCRIBIR EN UN Archivo PERO USANDO APPEND ESTE NO SOBREESCRIBE EL ARCHIVO SI CONTINUA DESPIUES DE LA ULTIMA LINEA 
try:
    with  open("archivo.txt","a") as f:
          f.write("\n") # para que de espeacion interlineal
          f.write("hola soy BuBuJa una linea nueva")
    with  open("archivo.txt","r") as f:
            print(f.read()) # lee todo el archivo   
  
except FileNotFoundError:
    print("No se ha encontrado el archivo")

"""

# creacion de un archivo 

#open("x.txt","x")

# escritura del archivo
try:
    with  open("x.txt","a") as f:
          f.write("\n") # para que de espeacion interlineal
          f.write("hola soy un nuevo archivo tienes algun problemas conmigo te debo algo, sabes soy mejor que tu !!!!")
except FileNotFoundError:
    print("No se ha encontrado el archivo")

# lectura 
try:
    with  open("x.txt","r") as f:
        print(f.read())   
except FileNotFoundError:
    print("No se ha encontrado el archivo")
