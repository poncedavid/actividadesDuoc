continuar="S"

print("-----------HELADERIA SANTA INÉS-----------------")
print("***     Cono Artesanal Simple        $1.000   ***")
print("***     Cono Artesanal Doble         $1.800   ***")
print("***     Vasito para niño             $800     ***")
print("-------------------------------------------------")
while(continuar=="S"):
    
    print("¡Bienvenido!")
    
    cantidadHelados= int(input("¿Cuantos helados desea?"))

    contHeladoSimple=0
    contHeladoDoble=0
    contHeladoNiño=0
   
    

    
    for i in  range (cantidadHelados):
        print("Presione -S- para Helado Simple ")
        print("Presione -D- para Helado Doble ")
        print("Presione -N- para Vasito")

        tipoHelado=input(f"¿Que tipo es el helano numero {i+1} ? ").upper()
       
        if (tipoHelado == "S"):
            contHeladoSimple=contHeladoSimple+1

        if(tipoHelado=="D"):
            contHeladoDoble=contHeladoDoble+1

        if(tipoHelado=="N"):
            contHeladoNiño=contHeladoNiño+1


    conoSimple=1000
    conoDoble=1800
    conoNiño=800

    precioSimple=contHeladoSimple*conoSimple
    precioDoble=contHeladoDoble*conoDoble
    precioNiño=contHeladoNiño*conoNiño
    
    precioFinal=precioSimple+precioDoble+precioNiño
    print("Helados de la Familia")
    print("------------------------------------------------------------------")
    print(f"contamos {contHeladoSimple} Helado/s Simple/s , ${precioSimple}")
    print(f"contamos {contHeladoDoble} Helado/s Simple/s , ${precioDoble}")
    print(f"contamos {contHeladoNiño} Helado/s Simple/s , ${precioNiño}")
    print("----------------------------------------------------------------")
    print(f"Su total a pagar es de: ${precioFinal}")
   

    continuar =  input("¿Desea continuar ( S / N) ?").upper()
    
print("¡Gracias! Vuelva pronto.")

