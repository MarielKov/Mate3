import matplotlib.pyplot as plt 
import numpy as np
datos_lins = np.array([1,2,3,4,5,6,7,8]) 
datos_cuads = datos_lins**2
plt.figure()
plt.plot(datos_lins, '-o', datos_cuads ,'-o') 
plt.plot([22,44,55],'--r')
plt.xlabel('Algún dato') 
plt.ylabel('Algún otro dato')
plt.title('Un título') 
plt.legend(['Dato1', 'Dato 2', 'Dato 3'])
plt.gca().fill_between(range(len(datos_lins)), datos_lins, datos_cuads, facecolor='green', alpha=0.25)
plt.show()
