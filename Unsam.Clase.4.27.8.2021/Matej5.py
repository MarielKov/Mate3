import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
M = {89 - 62, 62}
N = {103 - 62, 62}
U = 192
I = M & N
m = M - N
n = N - M

diagram = venn2(subsets = (1,1,1) , set_labels=('M', 'N'))
diagram.get_label_by_id('10').set_text(m)
diagram.get_label_by_id('01').set_text(n)
diagram.get_label_by_id('11').set_text(I)

plt.text(-0.80, -0.60,
         s="178 - (27 + 62 + 41) = " + str("48"),
         size=8,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.show()