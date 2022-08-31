import numpy as np

lista_de_listas=[ [-44,12], [12.0,51], [1300, -5.0]]
a = np.array(lista_de_listas)
print("Matriz original")
print(a)

suma = 0
#IMPLEMENTAR
# Calcular la suma de los elementos de a utilizando np.sum
#IMPLEMENTAR

suma=np.sum(a)
print(f"La suma de los elementos es:", {suma})

# Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
promedio=0
listam = [[0,0], [0,0]]
matriz = np.array(listam)
i = 0
j = 0
#IMPLEMENTAR
for i in matriz:
  for j in i:
   matriz[i][j] = matriz[i][j] + a[i][j]

promedio = np.mean(matriz)
print(f"Promedio (media) de los elementos:",{promedio})

# Calcular el promedio de los elementos de las primeras dos filas de utilizando slices (notación (:)) y np.mean
#IMPLEMENTAR
matriz2 = a[:2,:]
print(matriz2)
promedio = np.mean(matriz2)
print(f"Promedio (media) de los elementos:",{promedio})
