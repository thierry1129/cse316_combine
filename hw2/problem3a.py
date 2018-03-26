import csv
import matplotlib.pyplot as plt
import networkx as nx
from random import choice


## Erdos-Renyi Random Graph

Number_of_nodes=5242
m = 14484
# p=14484*2/(5242*(5242-1))

ERgraph=nx.Graph()
for n in range(Number_of_nodes): 
    ERgraph.add_node(n)

for edge in range(m):
    # pick a random node
    first_node = choice(ERgraph.nodes())
    possible_nodes = set(ERgraph.nodes())
    neighbours = ERgraph.neighbors(first_node) + [first_node]
    # remove the first node and all its neighbours from the candidates
    possible_nodes.difference_update(neighbours)
    # pick second node
    second_node = choice(list(possible_nodes))
    ERgraph.add_edge(first_node, second_node)


## Small-World Random Network

Number_of_nodes=5242
SWgraph=nx.Graph()
for n in range(Number_of_nodes): 
    SWgraph.add_node(n)
for n in range(Number_of_nodes-2): 
    SWgraph.add_edge(n, n+1)
    SWgraph.add_edge(n, n+2)
SWgraph.add_edge(Number_of_nodes-2,Number_of_nodes-1)
SWgraph.add_edge(Number_of_nodes-2,0)
SWgraph.add_edge(Number_of_nodes-1,0)
SWgraph.add_edge(Number_of_nodes-1,1)

for edge in range(4000):
    # pick a random node
    first_node = choice(SWgraph.nodes())
    possible_nodes = set(SWgraph.nodes())
    neighbours = SWgraph.neighbors(first_node) + [first_node]
    # remove the first node and all its neighbours from the candidates
    possible_nodes.difference_update(neighbours)
    # pick second node
    second_node = choice(list(possible_nodes))
    SWgraph.add_edge(first_node, second_node)


## Real World Collaboration Network

RWgraph=nx.Graph()
## read the graph from the collaboration file.
with open("collaboration_edges.txt") as tsv:
    tsv.readline()
    tsv.readline()
    tsv.readline()
    tsv.readline()
    for line in csv.reader(tsv, delimiter="\t"):
        RWgraph.add_edge(line[0], line[1])

edges = [e for e in RWgraph.edges_iter()]
for e in edges:
    if e[0] == e[1]:
        RWgraph.remove_edge(e[0],e[1])

print(RWgraph.number_of_nodes())








