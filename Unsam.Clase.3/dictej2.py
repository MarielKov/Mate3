dict = { "Manzana" : 12, "Limon" : 19, "Tomate" : 30 , "Naranja" : 24 , "Lechuga" : 43 }

fruta = input("Nombre:  ")
cant = int(input("Numero:  "))

while fruta in dict:

    x = dict.get(fruta)
    total = x * cant
    print(total)

    y = input("Y para continuar o N para terminar:   ")

    if y == "y" or y == "Y":
        fruta = input("Nombre:  ")
        cant = int(input("Numero:  "))

    elif y == "n" or y == "N":
       fruta = None
       print("Hasta Luego :)")

    else: 
        fruta = None
        print("ERROR")       





