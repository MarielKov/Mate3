# Importe el FigureCanvas desde el backend de su elección y adjunte el Artista de la figura a él. 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
from matplotlib.figure import Figure
  
fig = Figure() 
canvas = FigureCanvas(fig)
# Importar la biblioteca numpy para generar los números aleatorios. 
import numpy as np 
x = np.random.randn(10000)
# Ahora usa un método de figura para crear un artista de Axes; el artista Axes se agrega automáticamente al # contenedor de figuras fig.axes. Aquí "111" es de la convención de MATLAB: cree una cuadrícula con 1 fila # y 1 columna, y use la primera celda en esa cuadrícula para la ubicación de los nuevos ejes.
ax = fig.add_subplot(111)
# Llame al método Axes hist para generar el histograma; hist crea una secuencia de artistas Rectangle para cada barra de histograma y los agrega al contenedor Axes. Aquí "100" significa crear 100 contenedores (bins).
ax.hist(x, 100)
# Decora la figura con un título y guárdala.
ax.set_title('Normal distribution with $\mu=0, \sigma=1$') 
fig.savefig('matplotlib_histogram.png')
#plt.show()