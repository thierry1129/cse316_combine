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

deg_max=max(nx.degree(ERgraph).values())
all_nodes=nx.nodes_iter(ERgraph)
ERqkprime = {}
for k in range(deg_max):
    ERqkprime[k]=0
for node in all_nodes:
    for neighbor in nx.all_neighbors(ERgraph, node):
        ERqkprime[ERgraph.degree(neighbor)-1] += 1

ERqisum = 0
for key, value in ERqkprime.iteritems():
    ERqisum += value

ERexpected_e_d = 0
for key, value in ERqkprime.iteritems():
    ERexpected_e_d += key*value
ERexpected_e_d = float(ERexpected_e_d)/ERqisum

print('The expected excess degree of ER graph is %f' % (ERexpected_e_d))

fig = plt.figure()
ax = plt.gca()
ax.plot([i[0] for i in ERqkprime.items()],
    [float(i[1])/ERqisum for i in ERqkprime.items()], c='b', linestyle='None', marker='o', label='Erdos-Renyi')


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

deg_max=max(nx.degree(SWgraph).values())
all_nodes=nx.nodes_iter(SWgraph)
SWqkprime = {}
for k in range(deg_max):
    SWqkprime[k]=0
for node in all_nodes:
    for neighbor in nx.all_neighbors(SWgraph, node):
        SWqkprime[SWgraph.degree(neighbor)-1] += 1

SWqisum = 0
for key, value in SWqkprime.iteritems():
    SWqisum += value

SWexpected_e_d = 0
for key, value in SWqkprime.iteritems():
    SWexpected_e_d += key*value
SWexpected_e_d = float(SWexpected_e_d)/SWqisum

print('The expected excess degree of SW graph is %f' % (SWexpected_e_d))

ax.plot([i[0] for i in SWqkprime.items()],
    [float(i[1])/SWqisum for i in SWqkprime.items()], c='r', linestyle='None', marker='o', label='Small Wolrd')


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

deg_max=max(nx.degree(RWgraph).values())
all_nodes=nx.nodes_iter(RWgraph)
RWqkprime = {}
for k in range(deg_max):
    RWqkprime[k]=0
for node in all_nodes:
    for neighbor in nx.all_neighbors(RWgraph, node):
        RWqkprime[RWgraph.degree(neighbor)-1] += 1

RWqisum = 0
for key, value in RWqkprime.iteritems():
    RWqisum += value

RWqisum = 0
for key, value in RWqkprime.iteritems():
    RWqisum += value

RWexpected_e_d = 0
for key, value in RWqkprime.iteritems():
    RWexpected_e_d += key*value
RWexpected_e_d = float(RWexpected_e_d)/RWqisum

print('The expected excess degree of RW graph is %f' % (RWexpected_e_d))

ax.plot([i[0] for i in RWqkprime.items()],
    [float(i[1])/RWqisum for i in RWqkprime.items()], c='g', linestyle='None', marker='o', label='Real Wold')

plt.xlabel("Execss Degree k'")
plt.ylabel('Probabiliy qk')
plt.title('3ci) Excess Degree Distributions')
ax.set_yscale('log')
ax.set_xscale('log')
plt.legend(loc='lower left');
plt.savefig("excess_degree_Distribution.png")
plt.show()



