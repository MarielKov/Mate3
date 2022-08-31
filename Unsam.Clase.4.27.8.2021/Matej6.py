import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

L = {10 , 12, 8, 50}
C = {0, 12, 48, 50}
I = {19, 8, 48, 50}
N = {3}

def soloL(L, C, I):

    x = L - C
    y = L - I

    return (x & y)


L2 = soloL(L, C, I)
print(L2)

def soloC(L, C, I):

    x = C - L
    y = C - I

    return (x & y)


C2 = soloC(L, C, I)
print(C2)


def soloI(L, C, I):
    
    x = I - L
    y = I - C

    return (x & y)

I2 = soloI(L, C, I)
print(I2)

def soloLC(L , C):
  
    return (L & C)

LC = soloLC(L, C)
print(LC)


def soloCI(C , I):
    return (C & I)

CI = soloCI(C , I)
print(CI)


def soloLI(L , I):
    return (L & I)

LI = soloLI(L, I)
print(LI)


def soloLCI(L , C , I):
    return (L & C & I)

LCI = soloLCI(L, C, I)
print(LCI)

diagram = venn3(subsets = (1,1 ,1 ,1 ,1 ,1 ,1), set_labels=('Laptop', 'Celular', 'Ipod'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

diagram.get_label_by_id('100').set_text(L2)
diagram.get_label_by_id('010').set_text(C2)
diagram.get_label_by_id('001').set_text(I2)
diagram.get_label_by_id('110').set_text(LC - LCI)
diagram.get_label_by_id('011').set_text(CI - LCI)
diagram.get_label_by_id('101').set_text(LI - LCI)
diagram.get_label_by_id('111').set_text(LCI)

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

plt.text(-1.0, -0.50,
         f" Solo celular = {C2}",
         size=8,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.text(-1.0, -0.60,
         f" Ninguno de los 3 = {N}",
         size=8,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.text(-1.0, -0.70,
         f" Ipod y Laptop = {LI - LCI}",
         size=8,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )            

plt.show()