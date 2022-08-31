n = int(input("ingrese numero para lista:   "))
lista = []
m = int(input("ingrese numero para lista:   "))
lista2 = []

for i in range (n):

    p = input("ingrese una palabra:  ")
    lista.append(p)
    
for l in range (m):

    r = input("ingrese una palabra:  ")
    lista2.append(r)

i=0
l=0

for i in lista:
    for l in lista2:

        if lista[i] == lista2[l]:

         lista.remove(i)
  

print (f"{lista}") 
print (f"{lista2}") 

