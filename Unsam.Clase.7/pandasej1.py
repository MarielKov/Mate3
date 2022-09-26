"""1. Escribe un programa que pregunte al usuario por las ventas de un rango de años 
y muestre por pantalla una serie con los datos de las ventas indexada por los años,
antes y después de aplicarles un descuento del 10%."""

import pandas as pd

i = int(input("Ingrese un numero de entradas: "))

lista_precio = []
lista_art = []

for n in range(i):

    art = input("Ingrese nombre de articulo: ")
    precio = int(input("Ingrese precio: "))

    lista_precio.append(precio)
    lista_art.append(art)

lista_descuento = []

for n in lista_precio:

    desc = n * 0.1
    lista_descuento.append(desc)


dic = {"Articulo": lista_art, "Precio": lista_precio, "Descuento 10%":lista_descuento}   

df = pd.DataFrame(dic)
print(df)



