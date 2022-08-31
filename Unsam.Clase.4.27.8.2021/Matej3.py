from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

a = 125
i = 52
d = 257
aa = a - i
dd = d - i
venn2(subsets = (aa,dd,i) , set_labels=('Algebra 2', 'Deportes'))
plt.title('500 - (73 + 52 + 205) = 170') 

plt.show()