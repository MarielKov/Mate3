"""5. El archivo comercio_interno.csv contiene información sobre el comercio 
interno desde la década del 90. Escribe un programa que:
 a. Muestre por pantalla las dimensiones del Data Frame, el número de datos que contiene, 
 los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas 
 y las 10 últimas filas.
 b. Muestre por pantalla un gráfico de los datos de empleo por provincia y su relación
 con la columna valor.
 c. Muestre por pantalla la columna alcance_nombre ordenada alfabéticamente.
 d. Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor 
 e. Sume por alcance_nombre los valores de los años 2009 al 2019
 f. Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019
"""
import pandas as pd
import matplotlib.pyplot as plt



datos = pd.read_csv('Unsam.Clase.6/dataset/14.comercio_interno_1.csv', encoding='latin-1')

#a
print(datos.iloc[0:10 , 0:10])
print("\n")
print (datos.iloc[31274: , 0:10])
print("\n")
#c

orden = datos.sort_values('alcance_nombre',ascending=True)
print(orden['alcance_nombre'])
print("\n")
#d
orden2 = datos.sort_values('actividad_producto_nombre',ascending=True)
print(orden2['actividad_producto_nombre'])
print("\n")
#e

#f

#b
graf = pd.Series((datos.groupby('alcance_nombre')['valor']).sum())

graf.plot.barh()

plt.show()




