w= int(input("ingrese un inicio de rango:  "))

z= int(input("ingrese un limite de rango:  "))

t = z + 1

if t % 2 == 0 and w % 2 == 0: 
    j = t + 2
    x = range(w,j,2)

elif t % 2 != 0 and w % 2 == 0: 
     
     x = range(w,z,2)

elif  w % 2 != 0 and t % 2 == 0: 

     r = w + 1
     x = range(r,z,2)

else: 
    r = w + 1
    x = range(r,t,2)


y = list(x)
print(f"{y}")