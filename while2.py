# solicitar 2 numeros al usuario e imprimir los valores pares que hay entre dichos numeros

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1 

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1