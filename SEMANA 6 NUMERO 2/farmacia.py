#1) Una farmacia desea un programa para ingresar el valor de 
# compra y calcular lo siguiente: si el pago se efectúa al 
# “contado”, calcular un descuento del 
# 5%; pero si el pago es con “tarjeta” se incrementa un recargo 
# del 3% al valor de compra. 
# Calcular y visualizar el descuento o recargo según 
# sea el caso y el total a pagar de la compra.
# #

compra = float(input('Ingrese el valor de la compra '))
print("Seleccione metodo de pago contado o tarjeta")
capturardatos = str(input('Metodo de pago '))

if capturardatos == "contado":
    descuento = compra *0.05
    compra = compra - descuento
    print("Se aplico descuento ",compra)
    #El elfi va a existir solo si existe un if antes 
elif capturardatos == "tarjeta":
    aumento = compra *0.03
    compra = compra + aumento
    print("Se aplico aumento ",compra)
