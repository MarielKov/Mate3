import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

"""En una encuesta de 80 dueños de casa, se descubrió que:
 30 tenían al menos un perro.
 42 tenían al menos un gato.
 21 tenían al menos una mascota "otra" (pez, tortuga, reptil, hámster, etc.).
 20 Tenían perro(s) y gato (s).
 10 tenían gato(s) y mascota(s) otra.
 8 tenían perro(s) y mascota(s) otra.
 5 tenían los tres tipos de mascotas.
Haz un diagrama de Venn para ilustrar los resultados de la encuesta y responde: 
a. ¿Cuántos tenían perro(s) y gato(s) pero no mascota(s) "otra"?
b. ¿Cuántos solo tenían perro(s)?
c. ¿Cuántos no tenían mascotas?
d. ¿Cuántos dueños de mascota(s) otra también tenían perro(s) o gato(s), pero no ambos?
Puedes utilizar las letras en el siguiente diagrama de Venn para describir la región de cada uno de 
los conjuntos.

"""

duenios = 80
perro = {30,20,8,5} #A
gato = {42,20,10,5} #B
otras = {21,10,8,5} #C
PoG = 30 + 42
sin = 0
#i. A∩B
def funcinter(A ,B):
    
    x = A&B
    return x

interseccion = funcinter(perro , gato) 
print(interseccion)

#ii. A
print(perro)
#iii. A∪B
def funcuni(A ,B):
    
    y = A|B
  
    return(y)

union = funcuni(perro, gato) 
print(union)

#iv. A∩Bʹ

"""def funcinter2(A ,B):
    
    x = B.intersection_update(A)
    return x

interseccion2 = funcinter2(perro , gato) 
print(interseccion2)"""

#v. (A∩B)ʹ
def funcinter3(A ,B):
    
    x = not (A&B)

    return x

interseccion3 = funcinter3(perro , gato) 
print(interseccion3)

#vi. (A∪B)ʹ
def funcuni2(A ,B):
    
    y =  not (A|B)
   

    return y

union2 = funcuni2(perro, gato) 
print(union2)

#vii. Aʹ
def funcneg(A ):
    
   return not A

negativo = funcneg(perro) 
print(negativo)

#viii. Bʹ∪A

"""def funcuni3(A ,B, C):
    
    y =  (B.isdisjoint())|A
  
    return(y)

union3 = funcuni3(perro, gato) 
print(union3)
"""
def funcinter4(A ,B, C):
    
    x = A & B & C
    return x

perroGatoOtras = funcinter4(perro , gato, otras) 
print(perroGatoOtras)

def soloP(A, B, C):
    return (A - B) & (A - C)

soloP = soloP(perro, gato, otras)
print(soloP)

def soloG(A, B, C):
    return (B - A) & (B - C)

soloG = soloG(perro, gato, otras)
print(soloG)

def soloO(A, B, C):
    return (C - B) & (C - A)

soloO = soloO(perro, gato, otras)
print(soloO)

def soloPG(A, B):
    return (A & B)

soloPG = soloPG(perro, gato)
print(soloPG)

def soloPO(A, C):
    return (A & C)

soloPO = soloPO(perro, otras)
print(soloPO)

def soloGO(B, C):
    return (B & C)

soloGO = soloGO(gato , otras)
print(soloGO)

def gatosOPerros(A, B):
    suma = 0
    pog = ((A - B) | B)
    for elemento in pog:
        suma = suma + elemento
    return suma

gato_o_perro = gatosOPerros(perro, gato)
print(gato_o_perro)

diagram = venn3(subsets = (1,1 ,1 ,1 ,1 ,1 ,1), set_labels=('Perros', 'Gatos', 'Otras'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

diagram.get_label_by_id('100').set_text(soloP)
diagram.get_label_by_id('010').set_text(soloG)
diagram.get_label_by_id('001').set_text(soloO)
diagram.get_label_by_id('110').set_text(soloPG - perroGatoOtras)
diagram.get_label_by_id('011').set_text(soloGO - perroGatoOtras)
diagram.get_label_by_id('101').set_text(soloPO - perroGatoOtras)
diagram.get_label_by_id('111').set_text(perroGatoOtras)

plt.text(-0.80, -0.50,
         s=" Dueños = " + str(duenios) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )


plt.text(-0.80, -0.60,
         s=" Solo perros = " + str(soloP) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.text(-0.80, -0.70,
         s=" Perros y gatos = " + str(soloPG - perroGatoOtras) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.text(-0.80, -0.80,
         s=" Sin mascota = " + str(sin) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )

plt.text(-0.80, -0.90,
         s=" Perros o gatos = " + str(gato_o_perro) ,
         size=8,
         ha="left",
         va="bottom",
         bbox=dict(boxstyle="square",
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )



plt.title("Mascotas")
plt.show()

