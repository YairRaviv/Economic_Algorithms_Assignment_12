from typing import List
import numpy as np
import matplotlib.pyplot as plt

import networkx as nx

def build_graph(valuations: List[List[int]]):
    n = len(valuations)
    G = nx.DiGraph()
    for i in range(0,n):
        G.add_node(i)
    for i in range(0,n):
        indexes_of_max_houses = []
        max_value = max(valuations[i])
        for j in range(0, n):
            if valuations[i][j] == max_value:
                indexes_of_max_houses.append(j)
        for k in indexes_of_max_houses:
            G.add_edge(i , k)
    return G


if __name__ == '__main__':
    G = build_graph([[25,50,30,50,49] , [60,20,40,70,43] , [30,30,40,30,30], [13,90,90,30,30], [30,30,30,20,20]])
    val_map = {'A': 1.0,
               'D': 0.5714285714285714,
               'H': 0.0}
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    black_edges = [edge for edge in G.edges()]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                           node_color=values, node_size=500)
    nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    plt.show()