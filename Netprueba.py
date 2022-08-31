import networkx as nx
import matplotlib as plt

G = nx.Graph()

G.add_node('Hola mundo!')  
G.add_node('Nodo 1')  
G.add_edge('Hola mundo!', 'Nodo 1')
nx.draw(G)

plt.show()

#plt.use.style(´ggplot´)

