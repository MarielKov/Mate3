import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""2 . Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud mínima entre los vértic
es Z y A. Construir el grafo.
"""
G = nx.DiGraph()

nodos = np.arange(0, 8).tolist()
G.add_nodes_from(nodos)

G.add_edges_from([(0,6),(0,3),(0,1),(3,6),(1,6),(2,1),(3,4),(4,5),(7,4),(7,2),(5,7)])
labels={0:"A",1:"B",2:"C",3:"D", 4:"E",5:"F",6:"G",7:"Z"}



A_Z = nx.algorithms.dijkstra_path(G,0,7)

print("Ruta mas corta usando el algoritmo de Dijkstra entre a y e:\n", A_Z)

nx.draw_circular(G, labels=labels, arrows=True,
 node_shape = "s",
 node_color = "red", 
 edgecolors = "gray",
 font_size=8) 

nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G),
 edge_labels ={(0,6):'2', (0,3):'5', (0,1):'4',(3,6):'1',
 (1,6):'1',(2,1):'5',(3,4):'2',(4,5):'1',
 (7,4):'3',(7,2):'1',(5,7):'2'},
 font_color='gray')




plt.rcParams["figure.figsize"]=[7,7]


plt.axis('off')
plt.show()