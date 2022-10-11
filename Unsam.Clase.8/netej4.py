import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


G = nx.DiGraph()

nodos = ["A","B","C","D","E","F","G","H"]
G.add_nodes_from(nodos)

G.add_edges_from([("A","B"),("A","E"),("E","F"),("F","D"),("B","C"),("F","G"),("F","H")])

valores = {0 :"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
pos=nx.circular_layout(G)

A_H = nx.algorithms.dijkstra_path(G,"A","H")

print("Ruta mas corta usando el algoritmo de Dijkstra entre a y e:\n", A_H)

nx.draw_networkx(G, arrows= False,
 node_color = "red", 
 edgecolors = "gray",
 ) 

nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G),
 edge_labels ={("A","B") :4,("A","E"):9,("E","F"):1,("F","D"):2,("B","C"):4,("F","G"):9,("F","H"):5},
 font_color='gray')

plt.rcParams["figure.figsize"]=[7,7]

plt.axis('off')
plt.show()