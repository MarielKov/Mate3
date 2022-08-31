n = int(input("ingrese numero para lista:   "))
lista = []

for i in range (n):

    p = input("ingrese una palabra:  ")
    lista.append(p)
    print (f"{lista[i]} --- posicion {i}")  

print (f"{lista}")    

y = int(input("Que posicion desea cambiar?  "))

z = input("Que palabra desea poner en su lugar?  ")

lista.pop(y)
lista.insert(y, z)

print (f"{lista}")    