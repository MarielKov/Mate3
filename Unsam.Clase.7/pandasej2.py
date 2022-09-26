"""2. Escribe una función que reciba un diccionario con las notas de los alumnos de curso y
devuelva una serie con la nota mínima, la máxima, media y la desviación típica de cada uno.
"""

import pandas as pd

dic={}


i = int(input("Ingrese numero de alumnos: "))

def notas():
   
    lista_notas = []
    nombre = input("Nombre del alumno: ")

    for n in range(3):
        nota = int(input(f"Nota {n}: "))
        lista_notas.append(nota)
    
    return nombre, lista_notas

for n in range(i):
    suma = 0
    nombre , lista_notas = notas()
    minimo = min(lista_notas)
    print(minimo)
    maximo = max(lista_notas)
    print(maximo)
    media = round((sum(lista_notas) / 3),2)
    print(media)
    for n in lista_notas:
        exp = n**2
        suma = suma + exp

    desv = round((((suma / 3) - media**2)**0.5), 2)
    print(desv)
    dic.update({nombre : [minimo,maximo,media,desv]})

df = pd.Series(dic)
print(df)


