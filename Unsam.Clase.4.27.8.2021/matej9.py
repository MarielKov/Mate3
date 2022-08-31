import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles


""" 9. En una encuesta realizada en la ciudad de Buenos Aires, acerca de los medios de transporte más 
utilizados entre colectivos, subte o moto, se obtuvieron los siguientes resultados: de los 3200 
encuestados, 1950 utilizan el subte, 400 se desplazan en moto, 1500 van en colectivo, 800 se 
desplazan en colectivo y subte, además ninguno de los que se transporta en moto utiliza colectivo 
o subte.
a. El número de personas que solo utiliza el subte es….
b. Las persona que solo utilizan máximo 2 medios de transporte son…
"""
universo = 3200
subte = {1950,800,0,0 } #A
colectivo = {1500,800,0,0} #B
moto = {400,0,0,0} #C

def funcinter4(A ,B, C):
    
    x = A & B & C
    return x

interseccion = funcinter4(subte , colectivo, moto) 
print(interseccion)

def solos1(x, y):
    return (x & y)

soloSC = solos1(subte, colectivo)
print(soloSC)
soloCM = solos1(colectivo, moto)
print(soloCM)
soloSM = solos1(subte, moto)
print(soloSM)

def solos2(x, y, z):
    return (x - y) & (x - z)

soloM = solos2(moto,subte,colectivo)
print(soloM)

soloS = solos2(subte,colectivo, moto)
print(soloS)

soloC = solos2(colectivo,moto,subte)
print(soloC)


diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Colectivo", "Subte", "Motos"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloC)
diagram.get_label_by_id('010').set_text(soloS)
diagram.get_label_by_id('001').set_text(soloM)
diagram.get_label_by_id('110').set_text(soloSC - interseccion)
diagram.get_label_by_id('011').set_text(soloSM - interseccion)
diagram.get_label_by_id('101').set_text(soloCM - interseccion)
diagram.get_label_by_id('111').set_text(interseccion)


diagram.get_patch_by_id('101').set_alpha(1.0)
diagram.get_patch_by_id('101').set_color('white')
diagram.get_label_by_id('101').set_text('None')

diagram.get_patch_by_id('011').set_alpha(1.0)
diagram.get_patch_by_id('011').set_color('white')
diagram.get_label_by_id('011').set_text('None')

diagram.get_patch_by_id('111').set_alpha(1.0)
diagram.get_patch_by_id('111').set_color('white')
diagram.get_label_by_id('111').set_text('None')



# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universo = {universo}",
         size=10)

plt.text(-1.10, -0.50,
         s="Solo usan subte = " + str(soloS),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Usan 2 transportes = " + str(soloSC - interseccion),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.axis('on')  
plt.title("Transporte")
plt.show()