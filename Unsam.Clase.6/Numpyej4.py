"""4. La siguiente linea crea una matriz aleatoria de 5 por 5 con valores entre 0 y 1
matriz_aleatoria=np.random.rand(5,5)
print(matriz_aleatoria)
#Imprimir las posiciones (Fila y columna) de los elementos de la matriz que son mayores que 0.5
#IMPLEMENTAR"""

import numpy as np

matriz_aleatoria=np.random.rand(5,5)
print(matriz_aleatoria)

print("\n")

b = np.where(matriz_aleatoria>= 0.5)

print(b)