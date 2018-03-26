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

all_nodes=nx.nodes_iter(ERgraph)
sumci = 0
for node in all_nodes:
    if ERgraph.degree(node) > 1:
        eNi = 0
        neighbors = ERgraph.neighbors(node)
        for neighbor in neighbors:
            new_neigh = ERgraph.neighbors(neighbor)
            overlap = [val for val in new_neigh if val in neighbors]
            eNi += len(overlap)
        eNi = float(eNi)/2
        sumci += 2*eNi/(ERgraph.degree(node)*(ERgraph.degree(node)-1))

C = sumci/nx.number_of_nodes(ERgraph)

print('The average clustering coefficient of ER graph is %f' % (C))



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

all_nodes=nx.nodes_iter(ERgraph)
sumci = 0
for node in all_nodes:
    if SWgraph.degree(node) > 1:
        eNi = 0
        neighbors = SWgraph.neighbors(node)
        for neighbor in neighbors:
            new_neigh = SWgraph.neighbors(neighbor)
            overlap = [val for val in new_neigh if val in neighbors]
            eNi += len(overlap)
        eNi = float(eNi)/2
        sumci += 2*eNi/(SWgraph.degree(node)*(SWgraph.degree(node)-1))

C = sumci/nx.number_of_nodes(SWgraph)

print('The average clustering coefficient of SW graph is %f' % (C))

## Real World Collaboration Network

RWgraph=nx.Graph()

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

all_nodes=nx.nodes_iter(RWgraph)
sumci = 0
for node in all_nodes:
    if RWgraph.degree(node) > 1:
        eNi = 0
        neighbors = RWgraph.neighbors(node)
        for neighbor in neighbors:
            new_neigh = RWgraph.neighbors(neighbor)
            overlap = [val for val in new_neigh if val in neighbors]
            eNi += len(overlap)
        eNi = float(eNi)/2
        sumci += 2*eNi/(RWgraph.degree(node)*(RWgraph.degree(node)-1))

C = sumci/nx.number_of_nodes(RWgraph)

print('The average clustering coefficient of RW graph is %f' % (C))


