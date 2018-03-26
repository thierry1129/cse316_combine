import networkx as nx
from random import *
import matplotlib.pyplot as plt
import numpy


N0 = 5
p = 0.2
new_nodes = 995

G = nx.gnp_random_graph(N0, p)

for new_node in range(new_nodes):
    G.add_node(str(new_node)+'new')
    total_degrees = sum(G.degree(n) for n in G.nodes())
    for n in G.nodes():
        p_n = float(G.degree(n))/total_degrees
        if random()<p_n:
            G.add_edge(n, str(new_node)+'new')            

degree_sequence=sorted(nx.degree(G).values(),reverse=True)
Gdegrees=list(set([(i,degree_sequence.count(i)) for i in degree_sequence]))

fig = plt.figure()
ax = plt.gca()
ax.plot([i[0] for i in Gdegrees],
    [float(i[1])/(N0+new_nodes) for i in Gdegrees], c='b', linestyle='None', marker='.', label='Degree Distribution')


plt.xlabel("Degree k")
plt.ylabel('Probabiliy p_k')
plt.title('Degree Distributions')
ax.set_yscale('log')
ax.set_xscale('log')
plt.legend(loc='lower left');
plt.savefig("problem3a.png")
plt.show()
