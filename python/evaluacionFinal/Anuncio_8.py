contador=0
opcion=0

while opcion!=2:
    print("Ingrese su opcion:")
    print("1- Verificar palindromo.")
    print("2- Salir.")
    opcion=int(input())

    if opcion==1:
        palabra=str(input("Ingrese la palabra: ")).strip().upper()
        palabras=palabra.split()
        eliminaespacios="".join(palabras)
        invertir=""

        for l in range(len(eliminaespacios)-1,-1,-1):
            invertir+=eliminaespacios[l]

        for l in palabra:
            if (l.isalpha()):
                contador+=1

        if invertir==eliminaespacios:
            print("Es un palindromo")
            print("La cantidad de letras es: ",contador)

        else:
            print("No es un palindromo")
            print("La cantidad de letras es: ",contador)

    if opcion==2:
        print("Seleccionaste salir")
        break