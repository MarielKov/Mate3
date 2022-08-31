"""11. Una encuesta sobre 500 estudiantes inscriptos en una o más asignaturas de Matemática, Física y
Química durante un semestre, reveló los siguientes números de estudiantes en los cursos indicados:
Matemática 329, Física 186, Química 295, Matemática y Física 83, Matemática y Química 217, Física y
Química 63. Cuántos alumnos estarán inscriptos en:
a) Los tres cursos
b) Matemática pero no Química
c) Física pero no matemática
d) Química pero no Física
e) Matemática o Química, pero no Física
f) Matemática y Química, pero no Física
g) Matemática pero no Física ni Química"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

universo = 500
tres = universo - ((329 + 295 + 186) - (217 + 83 + 63))
print(tres)
matematicas = {329,83,217,tres} #A
quimica = {295,217,63,tres} #B
fisica = {186,83,63,tres} #C

matematicasSinQuimica = 329 + 83
print(matematicasSinQuimica)

fisicaSinMatematicas = 186 + 63
print(fisicaSinMatematicas)

fisicaSinQuimica = 186 + 83
print(fisicaSinQuimica)


def A_o_B(x, y):
    suma = 0
    x_o_y = ((x - y) | y)
    for elemento in x_o_y:
        suma = suma + elemento
    return suma

m_o_q = A_o_B(matematicas, quimica)
print(m_o_q)


def funcinter(A ,B, C):
    
    x = A & B & C
    return x

interseccion = funcinter(matematicas , quimica, fisica)
print(interseccion)

def solos1(x, y):
    return (x & y)

soloMQ = solos1(matematicas, quimica)
print(soloMQ)
soloMF = solos1(matematicas, fisica)
print(soloMF)
soloQF = solos1(fisica, quimica)
print(soloQF)

def solos2(x, y, z):
    return (x - y) & (x - z)

soloM = solos2(matematicas,fisica,quimica)
print(soloM)

soloQ = solos2(quimica,fisica,matematicas)
print(soloQ)

soloF = solos2(fisica,matematicas,quimica)
print(soloF)


diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Quimica", "Fisica", "Matematicas"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloQ)
diagram.get_label_by_id('010').set_text(soloF)
diagram.get_label_by_id('001').set_text(soloM)
diagram.get_label_by_id('110').set_text(soloMQ - interseccion)
diagram.get_label_by_id('011').set_text(soloMF - interseccion)
diagram.get_label_by_id('101').set_text(soloQF - interseccion)
diagram.get_label_by_id('111').set_text(interseccion)

transp = (soloMF | soloMQ | soloQF) - interseccion

transp2 = sum(transp)

suma = sum(soloQ | soloM | soloF)

noEstudia = suma - universo


print(noEstudia)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universo = {universo}",
         size=10)

plt.text(-1.10, -0.60,
         s="Matematicas sin quimica = " + str(matematicasSinQuimica),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s="Fisica sin matematicas = " + str(fisicaSinMatematicas),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.text(-1.10, -0.80,
         s="Fisica sin quimica = " + str(fisicaSinQuimica),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.90,
         s="Matematica o quimica = " + str(m_o_q),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="Matematica y quimica = " + str(soloMQ - interseccion),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s="Matematica solo = " + str(soloM),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.title("Materias")
plt.show()