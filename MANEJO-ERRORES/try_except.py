#try:
    #print("Intentar algo")
#except: # aqui se coloca el error que esperamos tal cu
    #print("capturar error")

try:
   num = 10 / 0
except ZeroDivisionError: 
    print("no se puede dividir por cero")


try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")

x = "m"
try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")
finally:
    print("Esto sera ejecutado siendo exitoso o no en el bloque")    