def factorial(x):
    vari = 1
    for i in range(x):
        vari = vari*(i+1)
    return vari

print(factorial(int(input("introduce un número entero positivo: "))))

