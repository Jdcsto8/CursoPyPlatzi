ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDOS,"r",encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("sin pedidos ")  
    except FileNotFoundError:
        print("\n todavia no existe hisotorial de pedidos")                  


