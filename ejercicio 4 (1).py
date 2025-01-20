def Media(x):
    sum = 0
    for i in x:
        sum = sum + i
    sum = sum/(len(x))
    return sum

while True:
    Lista=[]
    y = True
    while y != False:
        x = input("Intorduce el numero que quieras: ")
        if x != "":
            Lista.append(int(x))
        else:
            y = False
    print("Los números introducidos son:",Lista)
    print("La media de los números es:",round(Media(Lista),2))



