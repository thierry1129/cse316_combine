import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy
import operator
from resource import *
import scipy

from numpy import linalg as LA



karate = nx.read_gml('karate.gml', label='id')


sorted_bc=[1]
A = nx.adjacency_matrix(karate)
B=nx.to_dict_of_lists(karate)
actual_number_components=1
print(B)
print(nx.number_of_edges(karate))
# while not sorted_bc==[]:
#     modularity()
#     d_edge=nx.edge_betweenness_centrality(karate)
#     sorted_bc = sorted(d_edge.items(), key=operator.itemgetter(1))
#     e=sorted_bc.pop()
#
#     print "deleting edge:", e[0],
#     karate.remove_edge(*e[0])
#     prev_comp = 1
#     num_comp=nx.number_connected_components(karate)
#     print "...we have now ",num_comp," components"
#    nx.adj_matrix()
#     if num_comp>prev_comp:
#         prev_comp = num_comp;
#         #now compute the modularity of the graph
#         nx.connected_component_subgraphs.
#
#
#     if num_comp>actual_number_components:
#         actual_number_components=num_comp
#
#     for node in karate:
#
#
#     #print(modularity(karate))


