#tengo que crear un programa para una tienda
"""
este debe ser capaz de pedir
nombre del cliente
producto comprado
precio del producto
cantidad de productos
"""
#Despues debe calcular total de compra, si el totall es mayor o igual a 100.000$ el cliente recibe 10% de descuento

def sub_compra(producto, cantidad):
    valor_total = producto * cantidad
    return valor_total
def total_compra(total):
    condicion = input("Desea agregar mas productos?, si/no: ")
    if condicion == "si":
        producto = (input("agregue el otro producto: "))
        producto = float(productos[producto])
        cantidad = float(input("ingrese la cantidad a llevar: "))
        total = total + sub_compra(producto, cantidad)
        return total_compra(total)
    elif condicion == "no":
        return total
    else:
        print("error, no se escribio si o no")
        return total_compra(total)


productos = {
"arroz":4000,
"huevos":500,
"leche":3000,
"pechuga":20000,
"pan":5000,
"avena":6000,
"lenteja":4000,
"alberja":4300,
"frijol":5200,
"pasta":3500,
"atun":7000,
}
nombre = input("Escriba su nombre: ")

print("productos disponibles son: ", productos, "\nLos productos tienen el valor por kg")
producto = input("ingrese el producto deseado: ")
cantidad = input("ingrese la cantidad a llevar: ")
cantidad_float = float(cantidad)
producto = float(productos[producto])
total = sub_compra(producto, cantidad_float)
print(sub_compra(producto, cantidad_float))

total = total_compra(total)


if total >= 100000:
    total = total - total * 0.10
    print("como su compra es mayor a \n100000$, se hizo un descuento del 10%")
    print(nombre,":", "su valor total de compra es:", total)
else:
    print(nombre,":", "su valor total de compra es:", total)

