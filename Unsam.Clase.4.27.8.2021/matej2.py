
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

total = 600
a = 100
f= 450
fyi = 50
i = 50

venn3(subsets = (total, a,i , 0 ,f,0, fyi), set_labels=('Alumnos Totales', 'No estudia idiomas', 'Frances'))

plt.show()


