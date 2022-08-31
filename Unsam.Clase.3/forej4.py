
n = int(input("ingrese un numero:  "))

m = 1
w = 1

for i in range(n):
   
   v = m + w
   print(f"{m} + {w} = {v}" )
   m = w
   w = v

   
   