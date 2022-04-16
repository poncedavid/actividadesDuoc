listaVenta=[]
listaNombres=[]
acumVentas=0
ventaMenor=0
ventaMayor=0


while(True):

    print("opcion 1: Agregar Venta")
    print("opcion 2: Ver Resultados")
    print("opcion 3: Salir")

    opc=int(input("Ingrese su opcion:"))


    if(opc==1):

        nombre=input("Ingrese el nombre del nombre del vendedor: ")
        listaNombres.append(nombre)
        venta=float(input("¿Cuanto vendio el vendedor? :"))
        listaVenta.append(venta)

        if(venta<venta):
            ventaMenor=venta

        if(venta>venta):
            ventaMayor=venta



    if(opc==2):


        largo=len(listaNombres)
        for i in range(largo):
            print(f"Vendedor: {listaNombres[i]}  Venta realizada: ${listaVenta[i]}")

        largoVenta=len(listaVenta)
        for i in range(largoVenta):
            acumVentas=acumVentas+listaVenta[i]

        promVentas=(acumVentas)/largoVenta
        print(f"El promedio de ventas es {promVentas} ")
        
        #print(f"La venta mayor fue: ${ventaMayor}")
        #print(f"La venta menor fue: ${ventaMenor}")
        input("Presione enter para continuar.")


    if(opc==3):
        break