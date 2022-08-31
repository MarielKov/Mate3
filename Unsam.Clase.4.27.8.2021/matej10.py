""" 10. Se encuesta a 150 familias consultando por el nivel educacional actual de sus hijos.
Los resultados obtenidos son:
▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.
▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria
▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.
▪ 22 familias tienen hijos en Enseñanza Media y Universitaria.
▪ 72 familias tienen hijos en Enseñanza Media.
▪ 71 familias tienen hijos en Enseñanza Básica.
▪ 38 familias tienen hijos en Enseñanza Universitaria.
Con la información anterior, deducir:
a. El número de familias que solo tienen hijos universitarios.
b. El número de familias que tienen hijos solo en dos niveles.
c. El número de familias que tienen hijos que no estudian.
"""

import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

universo = 150
media = {72,30,22,10} #A
basica = {71,30,16,10} #B
universitaria = {38,16,22,10} #C

def funcinter(A ,B, C):
    
    x = A & B & C
    return x

interseccion = funcinter(media , basica, universitaria) 
print(interseccion)

def solos1(x, y):
    return (x & y)

soloMB = solos1(media, basica)
print(soloMB)
soloMU = solos1(media, universitaria)
print(soloMU)
soloBU = solos1(basica, universitaria)
print(soloBU)

def solos2(x, y, z):
    return (x - y) & (x - z)

soloM = solos2(media,basica,universitaria)
print(soloM)

soloB = solos2(basica,universitaria,media)
print(soloB)

soloU = solos2(universitaria,media,basica)
print(soloU)


diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Universitaria", "Basica", "Media"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloU)
diagram.get_label_by_id('010').set_text(soloB)
diagram.get_label_by_id('001').set_text(soloM)
diagram.get_label_by_id('110').set_text(soloBU - interseccion)
diagram.get_label_by_id('011').set_text(soloMB - interseccion)
diagram.get_label_by_id('101').set_text(soloMU - interseccion)
diagram.get_label_by_id('111').set_text(interseccion)

transp = (soloBU | soloMB | soloMU) - interseccion

transp2 = sum(transp)

suma = sum(soloB | soloM | soloU)

noEstudia =  suma - universo 


print(noEstudia)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universo = {universo}",
         size=10)

plt.text(-1.10, -0.50,
         s="Solo hijos universitarios = " + str(soloU),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Usan 2 transportes = " + str(transp2),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s="No estudia = " + str(noEstudia),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.title("Estudios por Familia")
plt.show()