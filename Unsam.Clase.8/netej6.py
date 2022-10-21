
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#plt.rcParams["figure.figsize"]=[7,7]

G = nx.DiGraph()

nodos = ["A","B","C","D","E","F","G","H","I"]
G.add_nodes_from(nodos)

G.add_edges_from([("A","B"),("A","F"),("A","D"),("B","C"),("B","G"),("C","H"),("C","D"),("D","I")
    ,("D","A"),("D","C"),("D","E"),("E","F"),("E","D"),("F","A"),("F","G"),("F","I"),("F","E")
    ,("G","H"),("G","B"),("G","F"),("H","I"),("H","A"),("H","C"),("H","G"),("I","B"),("I","D")
    ,("I","F"),("I","H")])


valores = {"A":[0,0],"B":[0,0.5],"C":[0,1.5],"D":[0,2],"E":[1,0],"F":[1,0.5],"G":[1,1],"H":[1,1.5],"I": [1,2]}

nx.draw_networkx(G,pos=valores,
 arrows= False,
 node_color = "red", 
 edgecolors = "gray",
 ) 

nx.draw_networkx_edge_labels(G,pos=valores,
 edge_labels ={("A","B"):12,("A","F"):5,("A","D"):6,("B","C"):7,("B","G"):8,("C","H"):5,
 ("C","D"):7,("D","I"):1,("D","A"):6,("D","C"):7,("D","E"):2,("E","F"):3,
 ("E","D"):2,("F","A"):5,("F","G"):6,("F","I"):15,("F","E"):3,("G","H"):3,
 ("G","B"):8,("G","F"):6,("H","I"):5,("H","A"):4,("H","C"):5,("H","G"):3,
 ("I","B"):2,("I","D"):1,("I","F"):15,("I","H"):5},
 )



plt.axis('off')
plt.show()