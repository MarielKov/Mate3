
lista = [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa") ] 
lista2 = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Londres", "Inglaterra"), ("Madrid", "España") ]

(pa , pb, pc, pd ) = lista
(ca, cb, cc, cd, ce ) = lista2

(a,b) = ca
(a,b) = cb
(a,b) = cc
(a,b) = cd
(a,b) = ce

n = int(input("Elija una opcion : 1- Agregar pasajero , 2- Agregar ciudad , 3- Ingrese DNI , 4- Ingrese pais , 5- Salir :     "))

if n == 1:
    pnn = input("Escriba nombre y apellido:   ")
    pnd = input("Escriba DNI:    ")
    des = input("Escriba destino:   ")

    pe = (pnn , pnd , des) 
   
    lista.append(pe) 

    print(lista)

elif n == 2:
    pais = input("Escriba pais de destino:   ")
    desb = input("Escriba destino:   ")

    destino = (desb, pais)
    lista2.append(destino) 

    print(lista2)
elif n == 3:
    pnd = input("Escriba DNI:    ")
    (a,b,c) = pa
    (a,b,c) = pb
    (a,b,c) = pc
    (a,b,c) = pd
    if pnd == b in pa:
      print(cd)
    elif pnd == b in pb:
      print(ca)
    elif pnd == b in pc:
      print(cb)
    elif pnd == b in pd:
      print(cc)
    else : print ("No existe destino o pasajero")
elif n == 4:
    pais = input("Escriba nombre y apellido:   ")

    if pais in ca:
      print(pb)
    elif pais in cb:
      print(pc)
    elif pais in cc:
      print(pd)
    elif pais in cd:
      print(pa)  
    else : print ("No existe destino o pasajero") 
elif n == 5:
    print("Adios")    
else: 
    print("ERROR")    