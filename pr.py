# Un grupo de jóvenes fue entrevistado para conocer sus preferencias de los
# siguientes medios de trasnporte: moto, auto y bicicleta. Los datos de la encuesta #fueron los siguientes: 
# 1. 5 jóvenes prefieren solamente la moto 
# 2. 38 jóvenes prefieren la moto
# #3. A 9 jóvenes no les gusta el automóvil como medio de transporte
#  #4. 3 jóvenes prefieren la moto y la bicicleta, pero no el auto 
# #5. 20 prefieren la moto y el auto, pero no la bicicleta 
# #6. A 72 no les gusta la bicicleta como medio de trasnporte 
# #7. Un solo joven, no prefiere ninguno de estos tres medios de transporte 
# #8. A 61 no les gusta la moto como medio de transporte 
M = {5,20,3,10}
A={46,20,10,14} 
B={0,3,10,14} 
U={1} 
#Muestro los conjuntos 
print(f"Los conjuntos son: \n M={M}, A={A}, B={B} y U={U}\n") 
#Funcion in 
print("Funcion in. Busco si 5 esta en el conjunto M: ") 
print(5 in M, end=" \n")
#Funcion len
print("Funcion len. Muestro el modulo de A: ") 
print(len(A)) 
#Funcion not 
print("Funcion not. Muestro si 10 no esta en B: ") 
print(10 not in B, end= "\n") 
#Funcion add 
print("Funcion add. Añado un elemento al conjunto U: ") 
print(U.add(5), end= "\n") 
print(U)
#Funcion remove 
print("Funcion remove. Elimino un elemento al conjunto U: ") 
print(U.remove(5), end= "\n") 
print(U)
#Funcion intersection 
print("Funcion intersection. Muestro la interseccion entre B y A: ") 
print(B&A, end=" \n") 
#Funcion union 
print("Funcion union. Muestro la union entre M y A: ")
print(M|A, end=" \n") 
#Funcion diferencia - 
print("Funcion diferencia. Aplico la funcion diferencia entre A y B: ")
print (A-B, end=" \n")
#Funcion ^ 
print("Funcion diferencia. Aplico la funcion diferencia simetrica entre A y B: ") 
print(A^B, end= " \n") 
#Funcion issubset 
print("Funcion issubset. Muestro si M es un subconjunto de A: ") 
print(M.issubset(A), end=" \n")