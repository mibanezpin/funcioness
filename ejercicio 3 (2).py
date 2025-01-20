def circulo(a):
    X = pow((3.1416*a), 2)
    return X

def cilindro(a, b):
    Y = circulo(a)*b
    return Y

Radio = float(input("Introduce un radio: "))
Altura = float(input("Introduce la altura: "))

print("El area del ciruclo es:", round(circulo(Radio), 2),"u")
print("El volumen del iclindro es:", round(cilindro(Radio, Altura), 2), "u")


