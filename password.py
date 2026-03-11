# genere una constante de texto que genere la contraseña. Luego pida al usuario que ingrese la contraseña. Mientras la contraseña no sea la correcta, debe continuar a pedir la contraseña. Si esta correcta, se deja de continuar el resto del programa

password = "Nikomore1"

texto = input("Ingrese la contraseña")

while password != texto:
    print("Contraseña invalida.")
    texto = input("Ingrese la contraseña.")
    
print("Acceso concedido !")