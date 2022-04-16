import random
largo_arreglo= 0
arreglo=[]

while largo_arreglo<=10:
    numero=random.randint(0,10)
    arreglo.append(numero)
    largo_arreglo+=1

print(arreglo)
numero_ingresado=int(input('Ingrese un numero: '))
if numero_ingresado in arreglo:
    print("El numero {} se encuentra dentro de la lista".format(numero_ingresado))
else:
    print('Lo siento el numero {} NO se encuentra en la lista'.format(numero_ingresado))