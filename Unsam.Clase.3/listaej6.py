n = int(input("ingrese numero para lista:   "))
lista = []
lista2 = []
x = []


for i in range (n):

    p = input("ingrese una palabra:  ")
    lista.append(p)
    

print (f"{lista}")   

lista2 = lista.copy()
lista2.reverse()

print(f"{lista2}")