dict = { "Ariana Salvatierra" : 12, "Leonardo Dias" : 19, "Mariel Kovinchich" : 30 , "Lidia Luna" : 24 , "Daiana Conlon" : 43 }

nom = input("Nombre:  ")
nota = int(input("Numero:  "))


while nota >= 0:

    if nom not in dict:
 
         dict.update({ nom : nota })
         nom = input("Nombre:  ")
         nota = int(input("Numero:  "))

    else : 
        nota = -1
        print("ERROR")  
    
if nota < 0:
        print (dict)
        print("Adios")  


