
#Ejercicio1#
#///////////////////
edadPersona = int(input("Ingrese su edad: "))

if(edadPersona >= 18):
    print("Ud es mayor de edad!   ")
else:
    print("Ud es menor de edad :(    ")


#Ejercicio2#
#//////////////////////

usuarioPrincipal =  input("Ingrese usuario:")
contraseñaUsuario = input("Ingrese contraseña usuario:")

if(usuarioPrincipal =="pedro" and contraseñaUsuario == "1234" ):
    print("Bienvenido pedro, que tengas un buen día.")
else:
    print("Ud a ingresado un usuario incorrecto")
if(usuarioPrincipal=="angel" and contraseñaUsuario == "a4s1" ):
    print("Bienvenido angel, que tengas un buen día.")


#Ejercicio 3#
#////////////////////////////

notaUno = float(input("ingrese nota 1 :"))
notaDos = float(input("ingrese nota 2 :"))
notaTres = float(input("ingrese nota 3 :"))

promedioNotas = (notaUno+notaDos+notaTres)/3

if(promedioNotas >= 4):
    print("Felicidades aprobaste con nota ", promedioNotas)
else:
    print("Lamentable, no aprobaste tu nota fue " , promedioNotas)

#////////////////////////////