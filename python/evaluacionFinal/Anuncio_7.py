a=0
b=1
try:
    print("---Para generar los números de la serie Fibonacci---")
    opc=int(input("Ingrese un numero entre 10 y 15: "))
    if opc<=15 and opc>=10:
        while b <=opc:
            print(b)
            a,b=b,a+b
    else:
        print("Ingresa un dato valido.")

except ValueError:
    print("Ingresa un numero valido.")
    
except NameError:
    print("Ingresa un dato valido.")