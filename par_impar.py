'''Determinar si un numero es par o inmpar'''


numero = int(input("Ingrese un numero entero: "))

residuo = numero % 2
if residuo == 0:
    print(f"{numero} es par ")
else:
    print(f"{numero} es impar")

print("Fin del programa")
