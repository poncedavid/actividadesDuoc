def comprobar_repetidos(primera_lista,segunda_lista):#funcion que le damos como argumentos las 2 listas dadas
    lista_elementos_repetidos=[]
    for i in primera_lista:
        for j in segunda_lista:
            if i==j:
                lista_elementos_repetidos.append(i)
    print(lista_elementos_repetidos)