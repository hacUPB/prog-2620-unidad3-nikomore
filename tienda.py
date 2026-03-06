''' una tienda ofrece una promocion, por la compra de 3 articulos, el costo del elemento de menor valor tiene un descuento del 50%'''

articulo1 = int(input("Ingrese el precio del articulo 1: "))
articulo2 = int(input("Ingrese el precio del articulo 2: "))
articulo3 = int(input("Ingrese el precio del articulo 2: "))

total = articulo1 + articulo2 + articulo3

if articulo1 < articulo2:
    temp = articulo1
else:
    temp = articulo2

if temp < articulo3:
    menor = temp
else:
    menor = articulo1

total = total -(menor * 0.5)
print(f"Debe pagar ${total}")