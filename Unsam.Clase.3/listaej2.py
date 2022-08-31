n = int(input("ingrese numero para lista:   "))
lista = []

for i in range (n):

    p = input("ingrese una palabra:  ")
    lista.append(p)

y = input("Que palabra desea buscar?  ")
x = lista.count(y)
print (f"La palabra esta {x} veces")    