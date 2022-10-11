import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


"""
G = nx.DiGraph()
nodos = np.arange(0, 8).tolist()

G.add_nodes_from(nodos)
G.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,7)])

pos={0:(10.0,10.0),1:(7.5,7.5),2:(12.5,7.5),3:(6.0,6.0),4:(9.0,6.0),5:(11.0,6.0),6:(14.0,6.0),7:(17.0,6.0)}
labels={0:"CEO",1:"Líder\nX",2:"Líder\nY",3:"A", 4:"B",5:"C",6:"D",7:"E"}
colors = ["snow","turquoise","orange","turquoise","turquoise","orange","orange","orange"]
edge_colors = ["turquoise","orange","turquoise","turquoise","orange","orange","orange"]
sizes = [1000, 2000, 2000, 1200, 1200, 1200, 1200, 1200]

nx.draw_networkx(G, pos=pos, labels=labels, arrows=True,
 node_shape = "s", node_size = sizes,
 node_color = colors, 
 edge_color = edge_colors, 
 edgecolors = "gray",
 font_size=8) 

plt.rcParams["figure.figsize"]=[7,7]
nx.draw_networkx_edge_labels(G, pos = pos, edge_labels={(0,1):'X', (0,2):'Y'}, font_color='gray')


nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels={(0,1):'3.0', (0,2):'4.5', (1,3):'6.0',(1,4):'8.5',
 (2,5):'10.5',(2,6):'7.0',(2,7):'9.5',(3,5):'1.5',
 (7,4):'6.0',(0,6):'5.0',(2,3):'6.5'}, font_color='gray')

plt.title("La empresa")
plt.axis('off')
plt.show()

"""
"""
G = nx.DiGraph()
nodos = np.arange(0, 8).tolist()

G.add_nodes_from(nodos)
G.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,7),(3,5),(7,4),(0,6),(2,3)])

labels={0:"CEO",1:"Líder\nX",2:"Líder\nY",3:"A", 4:"B",5:"C",6:"D",7:"E"}
colors = ["snow","turquoise","orange","turquoise","turquoise","orange","orange","orange"]
edge_colors = ["turquoise","orange","turquoise","turquoise","orange","orange","orange"]
sizes = [1000, 2000, 2000, 1200, 1200, 1200, 1200, 1200]

nx.draw_networkx(G, pos=nx.shell_layout(G), labels=labels, arrows=True,
 node_shape = "s", node_size = sizes,
 node_color = colors, 
 edge_color = edge_colors, 
 edgecolors = "gray",
 font_size=8) 

plt.rcParams["figure.figsize"]=[7,7]

nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels={(0,1):'3.0', (0,2):'4.5', (1,3):'6.0',(1,4):'8.5',
 (2,5):'10.5',(2,6):'7.0',(2,7):'9.5',(3,5):'1.5',
 (7,4):'6.0',(0,6):'5.0',(2,3):'6.5'}, font_color='gray')

plt.title("Proyecto Urgente")
plt.axis('off')
plt.show()
"""



