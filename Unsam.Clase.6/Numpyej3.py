""" 3. Generar una matriz de 7 por 9. Las primeras 3 columnas de la matriz tienen que tener el valor 0. La cuarta columna 
debe tener el valor 0.5, excepto por el último valor de esa columna, que tiene que ser 0.7. Las otras tres columnas 
deben tener el valor 1. Luego imprimir la matriz. Imprimir también el promedio de la última fila.
#IMPLEMENTAR
"""
import numpy as np

lista_matriz = [[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.5,1,1,1,1,1],[0,0,0,0.7,1,1,1,1,1]]

a = np.array(lista_matriz)
print("Matriz original")
print(a)
print("\n")
b = a[6:]
print(b)

print("\n")
c = b.mean() 
print(c)
