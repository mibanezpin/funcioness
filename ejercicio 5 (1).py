def listacuadrados(x):
    A = []
    for i in x:
        A.append(pow(i, 2))
    return A


while True:
    lista=[]
    i = True
    while i != False:
        x = input("Escribe el número que quieras ")
        if x != "":
            lista.append(int(x))
        else:
            i = False
    print("Los numeros introducidos son:",lista)
    print("Sus numeros al cuadradado son:",listacuadrados(lista))




