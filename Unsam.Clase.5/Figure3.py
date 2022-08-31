# Importar la biblioteca matplotlib 
import matplotlib.pyplot as plt
# Creamos  2 listas  con datos para el gráfico 
x = ['Python','Java', 'C', 'C++', 'Matlab', 'Octave'] 
usuarios = [10, 7, 15, 8, 9, 7]
# Uso de la capa de artista 
fig = plt.figure() # Se crea una figura 
ax = fig.add_subplot(111) # Nuevos ejes creados 
#el número 111 significa que sólo queremos una trama
# Interfazorientada a objetos 
# ax es el objeto y los elementos de gráfico se agregan utilizando diferentesmétodos de este objeto 
ax.bar(x, usuarios) 
ax.set_title('Usuarios de Lenguajes de Programación') 
ax.set_xlabel('Lenguaje de Programación') 
ax.set_ylabel('Número de usuarios')
plt.show ()
