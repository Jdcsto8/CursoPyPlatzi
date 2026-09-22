from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        # Mostrar el menu
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            #pedir un cafe
            pedir_cafe()
            #pass
        elif opcion == "2":
            # ver el historial
            #pass
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por havbeer tomado nuestros riquisimos cafes")
            break
        else:
            print("opcion invalida, escoga la opciones sugeridas")


if __name__ == "__main__":
    main()

