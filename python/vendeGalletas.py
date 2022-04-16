
acumuladorGalletas=0

print("¡BIENVENIDO!")
print("¡Somos la mejor fabrica de galletas!")
mayorista=input("¿Ud es un negocio mayorista (S/N)?")
if(mayorista=="S"):
    galletaClasica=input("¿Desea llevar Galletas Clasicas (S/N)?")
    if(galletaClasica=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioClasica=cantidadPaquete*900
        acumuladorGalletas=acumuladorGalletas+precioClasica

    galletaAvena=input("¿Desea llevar Galletas de Avena (S/N)?")
    if(galletaAvena=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioAvena=cantidadPaquete*1100
        acumuladorGalletas=acumuladorGalletas+precioAvena


    galleton=input("¿Desea llevar Galletones (S/N)?")
    if(galleton=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioGalleton=cantidadPaquete*600
        acumuladorGalletas=acumuladorGalletas+precioGalleton
else:
    galletaClasica=input("¿Desea llevar Galletas Clasicas (S/N)?")
    if(galletaClasica=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioClasica=cantidadPaquete*800
        acumuladorGalletas=acumuladorGalletas+precioClasica

    galletaAvena=input("¿Desea llevar Galletas de Avena (S/N)?")
    if(galletaAvena=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioAvena=cantidadPaquete*1000
        acumuladorGalletas=acumuladorGalletas+precioAvena


    galleton=input("¿Desea llevar Galletones (S/N)?")
    if(galleton=="S"):
        cantidadPaquete=int(input("Ingrese cantidades de paquetes: "))
        precioGalleton=cantidadPaquete*500
        acumuladorGalletas=acumuladorGalletas+precioGalleton

print(f"Ud debe cancelar${acumuladorGalletas}")