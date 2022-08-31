n = int(input("ingrese numero para lista:   "))
lista = []

for i in range (n):

    p = input("ingrese una palabra:  ")
    lista.append(p)
    

print (f"{lista}")    

y = input("Que palabra desea cambiar?  ")

lista.remove(y)

print (f"{lista}")    