dict = { "Ariana" : 123135642, "Leonardo" : 728917397, "Tobias" : 992837749 }

x = "y"
while x == "y" or x == "Y":

   nom = input("Nombre:  ")
   num = input("Numero:  ")

   dict.update({ nom : num })

   print(dict)

   x = input("Y para continuar o N para terminar:   ")

if x == "n" or x == "N":
     
     print("Hasta Luego :)")

else: print("ERROR")     