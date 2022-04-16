
acumuladorBidon=0
costoDespacho=2000
print("VENDEDOR AGUA PURIFICADA")
print("-----MANANTIAL-----")
bidonDiez=input("¿Desea llevar bidones de 10 Litros (S/N)?")
if(bidonDiez=="S"):
    
    cantidadDiez=int(input("Ingrese cantidad de bidones:"))
    totalBidon=cantidadDiez*2000
    acumuladorBidon=acumuladorBidon+totalBidon

bidonDoce=input("¿Desea llevar bidones de 20 Litros (S/N)?")
if(bidonDoce=="S"):
    cantidadDoce=int(input("Ingrese cantidad de bidones:"))
    totalBidon=cantidadDoce*4000
    acumuladorBidon=acumuladorBidon+totalBidon


if(acumuladorBidon>10000):
    print("tiene el despacho gratis")
    print(f"Debe pagar un total de ${acumuladorBidon}")
if(acumuladorBidon>0):
    totalPagar = acumuladorBidon + costoDespacho
    print(f"Debe pagar un total de ${totalPagar} " )
