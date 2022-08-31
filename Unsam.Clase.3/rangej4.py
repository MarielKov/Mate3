
w= int(input("ingrese un inicio de rango:  "))

z= int(input("ingrese un limite de rango:  "))

t = z + 1

x = range(w,t)
y = list(x)
print(f"{y}")
i =0
for i in range(len(y)-1, -1, -1):
 print(y[i], end=" ")
