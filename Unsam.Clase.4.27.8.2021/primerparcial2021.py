"""
En en una escuela de 1000 alumnos, se han evaluado literatura, matemática y biología, obte￾niéndose los siguientes resultados:
680 aprobaron literatura. Los datos de la evaluación de Literatura se registraron en un 
diccionario:


320 aprobaron biología. Los datos de la evaluación de Biología se registraron en una tupla: 

490 aprobaron matemática. Los datos de la evaluación de Matemática se registraron en una 
lista:


Responder:
a. cuántos aprobaron biología matemática y literatura.
b. cuántos aprobaron sólo literatura y matemática?
c. cuántos aprobaron sólo literatura?
d. cuántos aprobaron solo biología?
e. cuántos aprobaron sólo matemática?
f. cuántos aprobaron 2 de los 3 exámenes?
A modo de sugerencia se indican los pasos ordenados para la solución:
# 1. declaraciones
# 2. definir funciones de control (opcional) y otras (necesarias)
# 3. convertir en set las estructuras
# 4. Resolver las preguntas y resto de opciones para armar el gráfico
# 5. Definir diagrama de Venn, gráfico y respuestas.
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

universo = 1000

matematica = [34, 40, 61, 75, 87, 90, 103]

biologia = (40, 50, 60, 75, 34, 61)

literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
 "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}

set_matematica = set(matematica)

set_biologia = set(biologia)

def dic_a_conjunto(literatura):
    set_literatura = set()

    for n in literatura.values():
        set_literatura.add(n)
    return set_literatura

set_literatura = dic_a_conjunto(literatura)        

print(set_biologia)
print(set_literatura)
print(set_matematica)


def funcion_inter(x,y,z):
    return(x & y & z)

def soloXY(x ,y):
    return (x & y)

def soloX(x,y,z):
    return (x-y)&(x-z)

interseccion = funcion_inter(set_biologia,set_literatura,set_matematica)

soloMB = soloXY(set_matematica,set_biologia)
soloBL = soloXY(set_biologia,set_literatura)
soloML = soloXY(set_matematica,set_literatura)

soloM = soloX(set_matematica,set_biologia,set_literatura)
soloL = soloX(set_literatura,set_matematica,set_biologia)
soloB = soloX(set_biologia,set_literatura,set_matematica)



print("\n")
print(soloM)
print(soloL)
print(soloB)
print("\n")
print(soloMB)
print(soloBL)
print(soloML)
print("\n")
print(interseccion)

def suma(x):
    suma = 0
    for elemento in x:
        suma = suma + elemento
    return suma

sumaL = suma(soloL)
print(sumaL)

suma2de3= (soloBL | soloMB | soloML) - interseccion
print(suma2de3)

suma2x3 = suma(suma2de3)

plt.figure('Primer parcial 2021')


diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Matematicas", "Biologia", "Literatura"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloM)
diagram.get_label_by_id('010').set_text(soloB)
diagram.get_label_by_id('001').set_text(soloL)
diagram.get_label_by_id('110').set_text(soloMB - interseccion)
diagram.get_label_by_id('011').set_text(soloBL - interseccion)
diagram.get_label_by_id('101').set_text(soloML - interseccion)
diagram.get_label_by_id('111').set_text(interseccion)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universo}",
         size=10)

plt.text(-1.10, -0.20,
         s="Literatura, Matematicas y Biologia = " + str(interseccion),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s="Solo literatura y Matematicas = " + str(soloML -interseccion),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.text(-1.10, -0.40,
         s="Solo literatura = " + str(sumaL),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="Solo biologia = " + str(soloB),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Solo matematicas = " + str(soloM),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s="2 de 3 aprobados = " + str(suma2x3),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.show()