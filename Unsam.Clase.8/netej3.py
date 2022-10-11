import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""3. El plano muestra los puntos de conexión y las posibles líneas telefónicas en una urbanización. La zona quedará 
comunicada cuando dos puntos cualesquiera estén conectados. En rojo está indicado el precio de cada línea en miles 
de dólares. Calcular el diseño de la red más barata que conecte la zona.
"""
G = nx.DiGraph()

nodos = ["A","B","C","D","E","F","G","H","I","J","K","M","N"]
G.add_nodes_from(nodos)

G.add_edges_from([("A","B"),("A","C"),("A","D"),("B","E"),("B","C"),("C","D"),("C","E"),("C","F"),("D","F"),("D","G"),("E","I"),("E","H"),("E","F"),("F","I"),("F","G"),("G","J"),("H","K"),("H","I"),("H","L"),("I","J"),("I","L"),("J","L"),("J","M"),("K","L"),("K","N"),("L","N"),("L","M"),("M","N")])

valores = {0 :"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"M",12:"N"}
pos=nx.circular_layout(G)


nx.draw_networkx(G, arrows= False,
 node_color = "red", 
 edgecolors = "gray",
 ) 





plt.rcParams["figure.figsize"]=[7,7]


plt.axis('off')
plt.show()