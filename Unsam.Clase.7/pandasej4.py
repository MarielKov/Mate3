"""4. El archivo autos.xlsx contiene datos de precios de autos y stock. 
Construye el código necesario que emita el precio mínimo, el máximo y promedio. """

import pandas as pd


datos = pd.read_excel("Unsam.Clase.6/dataset/14.autos.xlsx")
df = pd.DataFrame(datos)
print(df["PRECIO"].min())
print(df["PRECIO"].max())
print(round(df["PRECIO"].mean(), 2))






