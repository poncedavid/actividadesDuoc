import Anuncio_6_funcion as f6
print("Opcion 1: para calcular area de un circulo")
print("Opcion 2: Primetro dee un cuadrado")
try:
    opc=int(input("----------Ingrese su opción: ---------- "))
    if opc==1:
        radio=int(input("Ingrese el radio del circulo: "))
        area=f6.calcular_area(radio)
        print(round(area))

    if opc==2:
        medida=int(input("Ingresa la medida de una de las caras del cuadrado: "))
        perimetro=f6.calcular_perimetro(medida)
        print(perimetro)

    if opc=="":
        print("Ingresa una opcion valida.")

    if opc==" ":
        print("Ingresa una opcion valida.")

    else:
        print("Ingresa una opcion valida")

except ValueError:
    print("Ingresa una opcion valida")

except NameError:
    print("Ingresa una opcion valida")