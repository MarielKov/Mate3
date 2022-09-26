"""4. El archivo autos.xlsx contiene datos de precios de autos y stock. 
Construye el código necesario que emita el precio mínimo, el máximo y promedio. """

import pandas as pd

datos = pd.read_csv("autos.csv")
df = pd.DataFrame(datos)
df.head()


