def binario(x):
    binar = []
    if x == 0:
        binar.append(x)
    else:
        while x != 1 or 0:
            binar.append(x%2)
            x = (x//2)
        binar.append(x)
        binar.reverse()
    return(binar)


while True:
    print(binario(int(input("Escribe el número entero: "))))





