
acumuladorServicio=0
desayuno=10000
globos=2000
tarjetaSaludo=1500
regaloSorpresa=3000

print("¡BIENVENIDOS!")
print("¡Vendemos los mejores desayunos!")
cantidadDesayuno=int(input("¿cuantos desayunos desea? "))
if(cantidadDesayuno>=1):
    servicioDesayuno=input("¿Desea incluir un desayuno (S/N)?")
    if(servicioDesayuno=="S"):
        acumuladorServicio=acumuladorServicio+desayuno
    servicioGloblos=input("¿Desea incluir un globo (S/N)?")
    if(servicioGloblos=="S"):
        acumuladorServicio=acumuladorServicio+globos
    servicioTarjeta=input("¿Desea incluir una tarjeta (S/N)?")
    if(servicioTarjeta=="S"):
        acumuladorServicio=acumuladorServicio+tarjetaSaludo
    servicioSorpresa=input("¿Desea incluir una sorpresa (S/N)?")
    if(servicioSorpresa=="S"):
        acumuladorServicio=acumuladorServicio+regaloSorpresa

precioFinal=acumuladorServicio*cantidadDesayuno

if(cantidadDesayuno>2):
    descuento=precioFinal*0.15
    totalPrecio=precioFinal-descuento
    print(f"¡Su total a pagar es $:{totalPrecio} con descuento, que lo disfrute!")
else:
    print(f"¡Su total cancelar ${precioFinal} , que lo disfrute!")