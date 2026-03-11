def menu():
    # No se debe permitir seleccionar una opcion que no esta
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. Suma\n3. Resta\n3. Multiplicacion\n4. Division")
        opcion = int(input("Selecione una opcion: "))
        if opcion < 1 or opcion > 4:
            print ("Opcion elegida no valida...\n")
    return opcion 

operacion = menu()
print(f"El usuario eligio la opcion {operacion}")

if operacion == 1:
    pass
elif operacion == 2:
    pass
elif operacion == 3:
    pass
