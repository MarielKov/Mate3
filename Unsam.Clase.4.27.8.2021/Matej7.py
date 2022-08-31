

import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles


A = {3, 7, 8, 8}
B = {8, 7, 4, 8}
C = {12, 8, 4, 8}
U = {6}

# 1
print(A)

# 2
print(C)

#3
def funcnot(A):
    
    z = not A
    print(z)
    return(z)

nt = funcnot(A) 
print(nt)

# 4
def funcinter(A ,B):
    
    x = A&B
    return(x)

inter = funcinter(A , B) 
print(inter)

# 5
def funcuni(A ,B, C):
    
    y = A|B|C
  
    return(y)

uni = funcuni(A, B, C) 
print(uni)

# 6
def funcdif(A ,B ,C, U):
    
    z = U | B | A
    y = z - C
    x = A & y
    return(y)
dif = funcdif(A, B, C, U)
print(dif)

# 7

def funcac(A ,B ,C):
    
    z = A & B & C
 
    return(z)

ac = funcac(A, B, C)
print(ac)

def funcneg(A ,B ,C):

    a = not A
    b = not B
    c = not C
    z = a & b & c
 
    return(z)

neg = funcneg(A, B, C)
print(neg)

diagram = venn3(subsets = (1,1 ,1 ,1 ,1 ,1 ,1), set_labels=('A', 'B', 'C'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

diagram.get_label_by_id('100').set_text(A)
diagram.get_label_by_id('010').set_text(B)
diagram.get_label_by_id('001').set_text(C)
diagram.get_label_by_id('110').set_text(A - ac)
diagram.get_label_by_id('011').set_text(B - ac)
diagram.get_label_by_id('101').set_text(C - ac)
diagram.get_label_by_id('111').set_text(ac)

plt.text(-0.80, -0.60,
         s=" Universo= " + str(U) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )
plt.show()