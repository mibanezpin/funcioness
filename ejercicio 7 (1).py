def recuento(a):
    a = (a.replace(",", "").replace(".", "").replace(":", "").replace(";", "")
     .replace("!", "").replace("¡", "").replace("?", "").replace("¿", "")
     .replace(")", " ").replace("(", " ").lower().split(" "))
    X={}
    for i in a:
        X[y]= (a.count(y))
    return(X)

def mayor(b):
    valormaximo=0
    indice = ""
    for i in b:
        if b[y] > valormaximo:  
            valormaximo = b[y]
            indice = y
    return((indice, valormaximo))

while True:
    print(mayor(recuento(input("Es:\n"))))






