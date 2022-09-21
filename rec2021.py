"""
En una encuesta a personas que tienen mascotas, dónde debían destacar las principales
características, se determinó que:
 55 son juguetones y son muy compañeros.
 48 son muy compañeros y son inteligentes.
 120 son juguetones e inteligentes.
 40 son juguetones, inteligentes y son muy compañeros.
Los datos se recabaron de la siguiente manera:
juguetones = (9, 25, 27, 38, 13, 6, 42)
inteligentes = [10, 8, 38, 42, 13, 27]
compañeros = {'a':27,'b':6, 'c':13, 'd':8, 'e':9,'f':5}
Responder:
a. ¿Cuántas mascotas son inteligentes solamente?
b. ¿Cuántas mascotas son sólo juguetones?
c. ¿Cuántas mascotas sólo son muy compañeros?
d. ¿Cuántas mascotas sólo son juguetones e inteligentes?
e. ¿Cuántas mascotas sólo son juguetones y son muy compañeros? 
f. ¿Cuántas mascotas sólo son inteligentes y son muy compañeros?
g. Calcular el conjunto universal
A modo de sugerencia se indican los pasos ordenados para la solución:
# 1. declaraciones
# 2. definir funciones de control (opcional) y otras (necesarias)
# 3. convertir en set las estructuras
# 4. Resolver las preguntas y el resto de operaciones para armar el gráfico 
# 5. Definir diagrama de Venn, gráfico y respuestas.
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

juguetones = (9, 25, 27, 38, 13, 6, 42)
inteligentes = [10, 8, 38, 42, 13, 27]
companieros = {'a':27,'b':6, 'c':13, 'd':8, 'e':9,'f':5}

set_juguetones = set(juguetones)

set_inteligentes = set(inteligentes)

def dic_a_conjunto(companieros):
    set_companieros = set()

    for n in companieros.values():
        set_companieros.add(n)
    return set_companieros

set_companieros = dic_a_conjunto(companieros)        

print(set_juguetones)
print(set_inteligentes)
print(set_companieros)

def funcion_inter(x,y,z):
    return(x & y & z)

def soloXY(x ,y):
    return (x & y)

def soloX(x,y,z):
    return (x-y)&(x-z)


interseccion = funcion_inter(set_companieros,set_inteligentes,set_juguetones)

soloCI = soloXY(set_companieros,set_inteligentes)
soloIJ = soloXY(set_inteligentes,set_juguetones)
soloJC = soloXY(set_companieros,set_juguetones)

soloC = soloX(set_companieros,set_inteligentes,set_juguetones)
soloI = soloX(set_inteligentes,set_juguetones,set_companieros)
soloJ = soloX(set_juguetones,set_companieros,set_inteligentes)

soloCI2 = soloCI - interseccion 
soloIJ2 = soloIJ - interseccion 
soloJC2 = soloJC - interseccion 

print("\n")
print(soloC)
print(soloI)
print(soloJ)
print("\n")
print(soloCI2)
print(soloIJ2)
print(soloJC2)
print("\n")
print(interseccion)


def suma(x):
    suma = 0
    for elemento in x:
        suma = suma + elemento
    return suma

def suma_dic(x):
    suma = 0
    for elemento in x.values():
        suma = suma + elemento
    return suma



suma_companieros = suma_dic(companieros) 

suma_juguetones = suma(juguetones)

suma_inteligentes = suma(inteligentes)

suma_inter = suma(interseccion)

universo = suma_companieros + suma_inteligentes + suma_juguetones
print(universo)


plt.figure('Recuperatorio 2021')


diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Compañeros", "Jueguetones", "Inteligentes"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloC)
diagram.get_label_by_id('010').set_text(soloJ)
diagram.get_label_by_id('001').set_text(soloI)
diagram.get_label_by_id('110').set_text(soloJC - interseccion)
diagram.get_label_by_id('011').set_text(soloIJ - interseccion)
diagram.get_label_by_id('101').set_text(soloCI - interseccion)
diagram.get_label_by_id('111').set_text(interseccion)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universo}",
         size=10)

plt.text(-1.15, -0.40,
         s="Compañeros, inteligentes y juguetones = " + str(suma_inter),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.show()                   