'''
Un almacen cobra 9000 por costos de enviio, pero ofrece el envio a domicilio gratis para compras superiores a 100000. en caso contrario,
no hay ningun descuento. solicite al usuario el valor de la compra y calcule el valor total a pagar 
'''


compra=int(input("Ingrese el valor de la compra"))
envio = 0
if compra < 100000:
   envio = 9000
   total = compra + envio 
   print(f"El valor a pagar es ${total}")
