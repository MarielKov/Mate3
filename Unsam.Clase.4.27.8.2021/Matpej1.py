#Un grupo de jóvenes fue entrevistado para conocer sus preferencias de los 
#siguientes medios de trasnporte: moto, auto y bicicleta. Los datos de la encuesta #fueron los siguientes:
#1. 5 jóvenes prefieren solamente la moto
#2. 38 jóvenes prefieren la moto 
#3. A 9 jóvenes no les gusta el automóvil como medio de transporte
#4. 3 jóvenes prefieren la moto y la bicicleta, pero no el auto 
#5. 20 prefieren la moto y el auto, pero no la bicicleta 
#6. A 72 no les gusta la bicicleta como medio de trasnporte 
#7. Un solo joven, no prefiere ninguno de estos tres medios de transporte 
#8. A 61 no les gusta la moto como medio de transporte 


import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles


M={5,20,3,10} 
A={46,20,10,14} 
B={0,3,10,14} 
U={1} 
#Muestro los conjuntos 
print(f"Los conjuntos son: \n M={M}, A={A}, B={B} y U={U}\n") 

#Funcion in 
print("Funcion in. Busco si 5 esta en el conjunto M: ") 
def funcin(M):
    
  y = 5 in M
  return(y)

x = funcin(M) 
print(x)


#Funcion len
print("Funcion len. Muestro el modulo de A: ") 

def funclen(A):
    
  y = len(A)
  return(y)

x = funclen(M) 
print(x)


#Funcion not 
print("Funcion not. Muestro si 10 no esta en B: ") 
def funcnot(B):
    
  y = 10 not in B
  return(y)

x = funcnot(B) 
print(x)

#Funcion add 
print("Funcion add. Añado un elemento al conjunto U: ") 

def funcadd(u):
    
  y = U.add(5)
  return(y)

x = funcadd(U) 
print(x)

#Funcion remove 
print("Funcion remove. Elimino un elemento al conjunto U: ") 

def funcremove(u):
    
  y = U.remove(5)
  return(y)

x = funcremove(U) 
print(x)


#Funcion intersection 
print("Funcion intersection. Muestro la interseccion entre B y A: ") 

def funcinter(B ,A):
    
  y = B&A
  return(y)

x = funcinter(B , A) 
print(x)

#Funcion union 
print("Funcion union. Muestro la union entre M y A: ")

def funcint(M ,A):
    
  y = M|A
  return(y)

x = funcint(M , A) 
print(x)


#Funcion diferencia - 
print("Funcion diferencia. Aplico la funcion diferencia entre A y B: ")

def funcinter(A ,B):
    
  y = A-B
  return(y)

x = funcinter(A , B) 
print(x)


#Funcion ^ 
print("Funcion diferencia. Aplico la funcion diferencia simetrica entre A y B: ") 

def funcinter(A , B):
    
  y = A^B
  return(y)

x = funcinter(A, B) 
print(x)

#Funcion issubset 
print("Funcion issubset. Muestro si M es un subconjunto de A: ") 

def funciss(M , A):
    
  y = M.issubset(A)
  return(y)

x = funciss(M , A) 
print(x)


def suma_moto(M):
    sum = 0
    for z in M:
        sum = sum + z
    return sum

moto = suma_moto(M)

print(moto) 


def suma_auto(A):
    sum = 0
    for z in A:
        sum = sum + z
    return sum

auto = suma_auto(A)

print(auto) 

def suma_bici(B):
    sum = 0
    for z in B:
        sum = sum + z
    return sum

bici = suma_bici(B)

print(bici)

total = bici + auto + moto
print(total)

def soloB(M, A, B):

    x = B - A
    y = B - M

    return (x & y)


B2 = soloB(M, A, B)
print(B2)

def soloM(M, A, B):

    x = M - B
    y = M - A

    return (y & x)


M2 = soloM(M, A, B)
print(M2)


def soloA(M, A, B):
    
    x = A - B
    y = A - M

    return (y & x)

A2 = soloA(M, A, B)
print(A2)

def soloBA(b , a):
  
    return (b & a)

BA = soloBA(B, A)
print(BA)


def soloAM(a , m):
    return (a & m)

AM = soloAM(A , M)
print(AM)


def soloMB(m , b):
    return (m & b)

MB = soloMB(M, B)
print(MB)


def soloMBA(m , a , b):
    return (m & a & b)

MBA = soloMBA(M, A, B)
print(MBA)



diagram = venn3(subsets = (1,1 ,1 ,1 ,1 ,1 ,1), set_labels=('Motos', 'Bicicleta', 'Autos'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

diagram.get_label_by_id('100').set_text(M2)
diagram.get_label_by_id('010').set_text(B2)
diagram.get_label_by_id('001').set_text(A2)
diagram.get_label_by_id('110').set_text(MB - MBA)
diagram.get_label_by_id('011').set_text(AM - MBA)
diagram.get_label_by_id('101').set_text(BA - MBA)
diagram.get_label_by_id('111').set_text(MBA)

plt.text(-0.80, -0.60,
         s=" Ninguno de los 3 = " + str("1"),
         size=8,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),) )
plt.show()

 
