import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
datos_lins = np.array([1,2, 3, 4, 5, 6, 7, 8]) 
datos_cuads = datos_lins**2
plt.figure() 
datos_observados = np.arange('2021-03-01','2021-03-09',dtype='datetime64[D]') 
datos_observados = list(map(pd.to_datetime, datos_observados))
plt.plot(datos_observados, datos_lins, '-o', datos_observados,datos_cuads, '-o')
x = plt.gca().xaxis
for item in x.get_ticklabels(): item.set_rotation(45)
plt.subplots_adjust(bottom=0.25)
ax = plt.gca() 
ax.set_xlabel('Dato') 
ax.set_ylabel('Unidades') 
ax.set_title('Rendimiento exponencial ($x^2$) frente al lineal ($x$)')
plt.show()

