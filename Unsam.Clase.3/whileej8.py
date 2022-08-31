n = int(input("ingrese un numero par:  "))
while (n % 2 != 0):

     n = int(input("ingreso un numero impar, intente de nuevo:  "))


     while (n % 2 == 0): 

         p = input("Desea continuar? Si (s) No (n) :  ")

         if(p == "s") or (p == "S") :

          n = int(input("ingrese un numero par:  "))
  
     
         elif (p == "n") or (p == "N"):

          print("Adios")

         else: 
          print("ERROR")  
     

        
    