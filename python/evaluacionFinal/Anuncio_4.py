import random
numeros=[[],[]]
largo=1
total=0
try:
    #Primera_lista.
    num1=int(input("Ingresa un numero entre 3 y 6 para la lista A : "))

    if num1 >=3 and num1 <=6:
        print("Se agrego el numero ",num1," a la lista A")
        numeros[0].append(num1)

        for i in range (10):
            numero=random.randint(1,100)
            numeros[0].append(numero)

        total=sum(numeros[0])
        promedio=total/11
        print("Los Numeros agregadoa aleatoriamente a la lista A son : ",numeros)
        print("La suma de los numeros en su lista A es: ",total)
        print("El promedio de los numeros agregados en su lista A son: ",round(promedio))

    else:
        print("Ingresa un numero entre 3 y 6 ")
    #Segunda_lista
    num2=int(input("Ingresa un numero entre 3 y 6 para la lista B :  "))

    if num2 >=3 and num2 <=6:
        print("Se agrego el numero ,",num2," a la lista")
        numeros[1].append(num2)

        for i in range (10):
            numero=random.randint(1,100)
            numeros[1].append(numero)

        total=sum(numeros[1])
        promedio=total/11
        print("Los Numeros agregados aleatoriamente a la lista A son : ",numeros)
        print("La suma de los numeros en su lista A es: ",total)
        print("El promedio de los numeros agregados en su lista A son: ",round(promedio))
        print("=================================================================================================")
        sumafinal=sum(numeros[1]+numeros[0])
        promediofinal=sumafinal/22
        print("La suma total de ambas listas es de: ",sumafinal)
        print("El promedio final de ambas listas es de: ",round(promediofinal))
        print("================================================================================================")
    else:
        print("Ingresa un numero entre 3 y 6")


except ValueError:
    print("Ingresa datos validos.")
except NameError:
    print("Ingresa datos validos.")
