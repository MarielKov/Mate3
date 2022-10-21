
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"]=[7,7]

G = nx.DiGraph()

nodos = ["A","B","C","D","E","F","G","H","I"]
G.add_nodes_from(nodos)

G.add_edges_from([("A","B"),("A","F"),("A","I"),("B","C"),("B","F"),("B","I"),("C","D"),("C","I"),("D","I"),("D","H"),("D","G"),("E","F"),("E","H"),("E","G"),("F","G"),("F","I"),("G","H"),("G","I"),("H","I")])

#valores = {0 :"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
pos = {"A":[0,0],"B":[0,0.5],"C":[0,1.5],"D":[0,2],"E":[1,0],"F":[1,0.5],"G":[1,1],"H":[1,1.5],"I": [1,2]}

x = 68
y= x-36

G.add_edge("B","G",weight = y)

A_B = nx.algorithms.dijkstra_path(G,"A","B")
A_C = nx.algorithms.dijkstra_path(G,"A","C")
A_D = nx.algorithms.dijkstra_path(G,"A","D")
#A_E = nx.algorithms.dijkstra_path(G,"E","A")
A_F = nx.algorithms.dijkstra_path(G,"A","F")
A_G = nx.algorithms.dijkstra_path(G,"A","G")
A_H = nx.algorithms.dijkstra_path(G,"A","H")
A_I = nx.algorithms.dijkstra_path(G,"A","I")

print("Ruta mas corta usando el algoritmo de Dijkstra entre a y b:\n", A_B)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y c:\n", A_C)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y d:\n", A_D)
#print("Ruta mas corta usando el algoritmo de Dijkstra entre a y e:\n", A_E)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y f:\n", A_F)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y g:\n", A_G)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y h:\n", A_H)
print("Ruta mas corta usando el algoritmo de Dijkstra entre a y i:\n", A_I)

nx.draw_networkx(G,pos=pos,
 arrows= False,
 node_color = "red", 
 edgecolors = "gray",
 ) 

nx.draw_networkx_edge_labels(G,pos=pos,
 edge_labels ={("A","B"):20,("A","F"):34,("A","I"):45,("B","C"):20,("B","F"):10,("B","I"):26,("C","D"):28,("C","I"):22,("D","I"):13,("D","H"):19,("D","G"):18,("E","F"):22,("E","H"):25,("E","G"):12,("F","G"):30,("F","I"):12,("G","H"):16,("G","I"):14,("H","I"):32},
 font_color='gray')



plt.axis('off')
plt.show()