import numpy as nu
cont=0
vuelo = nu.empty ( [7,6] , dtype = 'object')
datospasajeros=[]
for i in range(7):
    for j in range(6):
        cont= cont + 1
        vuelo [i,j]= str(cont)
cont=0        

datospasajeros = nu.empty([43,4] , dtype = 'object')
for i in range(43):
    cont=cont
    for j in range(4):
        if(i==0):
            if(j==0):
                datospasajeros[i,j] = str("nombre")
            if(j==1):
                datospasajeros[i,j] = str("rut")   
            if(j==2):
                datospasajeros[i,j] = str ("telefono")
            if(j==3):
                datospasajeros[i,j] = str("banco")
        else:
            datospasajeros [i,j] = str ("-")
                   
while (True):
    print("Bienvenidos al terminal de ventas DuocUc ")
    print("opc1: ver asientos disponibles")
    print("opc2: comprar asiento")
    print("opc3: anular vuelo")
    print("opc4: modificar datos del pasajero")
    print("opc5 : Salir")

    try:
        opcion =int(input("ingrese su opcion del 1-5"))
    except:
        opcion=0

        if(opcion==1):
         print("opcion 1 : ver asientos disponibles ")
         print(" opcion 2 : ver listados de pasajeros")
         print("opcion 3 : salir")


         try:
            subopcion = int(input("ingrese su opcion 1-3"))
         except:
            subopcion=0

         if(subopcion==1):
            print(" ver asientos disponibles en el vuelo...")
            for i in range(7):
                print(f"{vuelo[i,1]}\t{vuelo[i,2]}\t{vuelo[i,3]}\t{vuelo[i,4]}\t{vuelo[i,5]}")        
         if(subopcion==2):
            print("ver listado de pasajeros")
            for i in range(43):
                if(i ==0):
                     print(f"X   {datospasajeros[i,0]}\t-\t {datospasajeros[i,1]}\t-\t {datospasajeros[i,2]}\t-\t {datospasajeros[i,3]}")
                else:
                        print(f"{i}  | {datospasajeros[i,0]}\t-\t {datospasajeros[i,1]}\t-\t {datospasajeros[i,2]}\t-\t {datospasajeros[i,3]}")

        input("::::::::precione enter para continuar:::::::")
        
        
        if(opcion==2):
            print("comprar asiento")

            try:
                tx_numeroAsiento= int(input(" ingrese su numero dr asiento :"))
                if ( tx_numeroAsiento > 42 or tx_numeroAsiento == 0):
                    input(" error en seleccionar du asiento.... press enter para contianuar")
                    opc = 0
                else:
                    opc =1    
            except:
                opc = 0
                input(" error el dato ingresado no es valido .....")
            if ( opc==1):
                cont=0
                for i in range(7):
                    for j in range(6):
                        cont = cont+ 1
                        if (cont == tx_numeroAsiento):
                            if ( vuelo [i,j]== "X"):
                                opc=0
                                input(" este asiento ya esta reservado.... enter para continuar")
                            else:
                                opc= 1
                if ( opc ==1):
                    for i in range (7):
                        for j in range (6):
                            if(vuelo[i,j] == str (tx_numeroAsiento)):
                                vuelo[i,j] ="X"


                                tx_nombredelPasajero = input("ingrese el nombre del pasajero")
                                tx_rutDelpasajero = input("ingrese el rut del pasajero")
                                tx_TelefonoPasajero = input ( " ingrese el telefono del pasajero ")
                                tx_BancodelPasajero = input (" ingrese el banco del pasajero ")

                                datospasajeros[int(tx_numeroAsiento),0] = str(tx_nombredelPasajero).upper()
                                datospasajeros[int(tx_numeroAsiento),1] = str(tx_rutDelpasajero).upper()
                                datospasajeros[int(tx_numeroAsiento),2] = str (tx_TelefonoPasajero).upper()
                                datospasajeros[int(tx_numeroAsiento),3] = str(tx_BancodelPasajero).upper()
                                input(" Su vuelo a sido comprado con exito .... enter para continuar ")
        if(opcion==3):
            print("anular vuelo ?")
            tx_numeroAsiento = input ( " ingrese el numero de asiento a anular")
            cont = 0
            for i in range(7):
                for j in range(6) :
                    cont= cont + 1
                    if ( cont== tx_numeroAsiento):
                        vuelo [i,j]= str (cont)
                        datospasajeros [int(tx_numeroAsiento),0] = "."
                        datospasajeros [int(tx_numeroAsiento),1] = "."
                        datospasajeros [int(tx_numeroAsiento),2] = "."
                        datospasajeros [int(tx_numeroAsiento),3] = "."                      

    if(opcion==4):
        print("modificar datos del pasajero :")
        tx_numeroAsiento = int(input(" ingrese el numero del asiento del pasajero :"))
        cont=0
        for i in range(7):
            for j in range(6):
                cont = cont + 1
                if ( cont == tx_numeroAsiento):
                    if ( vuelo[i,j]== str(tx_numeroAsiento)):
                        input ( " asiento ingresado vacio , precione enter para contianur :")
                    else:
                        opc= 1
        if(opc==1):
            while(True):
                try:
                    print(" opcion 1 : modificar nombre")
                    print(" opcion 2 : modificar rut :" )
                    print(" opcion 3 : modificar telefono:")
                    print(" opcion 4 : modificar banco : ")
                    print(" opcion 5 : salir ")

                    try:
                        subopcion = int(input("ingrese la opcion del 1-5"))
                    except:
                        subopcion = 0   

                    if(subopcion == 1):
                        print(f" nombre actual {datospasajeros [int(tx_numeroAsiento),0]}  asiento : {tx_numeroAsiento}")
                        dato = input(" ingrese el nuevo nombre :")
                        datospasajeros[int(tx_numeroAsiento),0] = dato.upper()
                    if(subopcion == 2):
                        print(f" rut actual {datospasajeros [int(tx_numeroAsiento),1]}  asiento : {tx_numeroAsiento}")
                        dato = input(" ingrese el nuevo rut :")
                        datospasajeros[int(tx_numeroAsiento),0] = dato.upper()
                    if(subopcion == 3):
                        print(f" telefono actual {datospasajeros [int(tx_numeroAsiento),2]}  asiento : {tx_numeroAsiento}")
                        dato = input(" ingrese el nuevo telefono :")
                        datospasajeros[int(tx_numeroAsiento),0] = dato.upper()
                    if(subopcion == 4):
                        print(f" banco actual {datospasajeros [int(tx_numeroAsiento),3]}  asiento : {tx_numeroAsiento}")
                        dato = input(" ingrese el nuevo banco :")
                        datospasajeros[int(tx_numeroAsiento),0] = dato.upper()
                    if(subopcion==5):
                        break
                except:
                    input(" error no controlado..... favor presione enter para contianuar.....")

    if(opcion==5):
        print(" muchas gracias por operar con nosotros..")
        print(" hasta pronto")
        break
                    

                                   
                            












