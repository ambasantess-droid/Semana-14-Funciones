def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje / 100
    total = precio - descuento
    return total

precio = float(input("Ingrese el precio de la compra: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

resultado = calcular_descuento(precio, porcentaje)

print("El total a pagar con descuento es:", resultado)