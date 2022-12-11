import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

class Node:
    def __init__(self):
        pass

class Edge:
    def __init__(self):
        pass



'''
G = nx.Graph()

G.add_node(1)
G.add_node('p')
G.add_node('HI')

G.add_nodes_from([2, 4])

G.add_edge(1, 2)
G.add_edge(1,'p')
G.add_edges_from([[1,'HI'], [1,4]])

print(G.nodes())


#G=nx.path_graph(4)

# same output

#G=nx.Graph()
#nx.add_path(G, [0,1,2,3])

#G.remove_edge(1, 2)
#G.remove_node(3)

#G.remove_edges_from([(0,1), (2,3)])
#G.remove_nodes_from([1,2,3])

#G = nx.erdos_renyi_graph(100, 0.01)
G = nx. watts_strogatz_graph(30, 3, 0.1)


nx.draw(G, with_labels=True, node_color='lightblue', edge_color = 'red')

print("노드 수 : ", G.number_of_nodes())
print("에지 수 : ", G.number_of_edges())
plt.show()
'''

data = pd.read_csv('test.csv', encoding = 'utf-8-sig')

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

g = nx.Graph()
print(data.head())
g = nx.from_pandas_edgelist(data.head(50), source = 'index', target = 'nouns', edge_attr='Probability')

plt.figure(figsize = (10, 10))
pos = nx.spring_layout(g, k = 0.15)
nx.draw_networkx(g, pos, node_size = 100, node_color = 'blue', font_family=font, font_size = 20)


plt.show()