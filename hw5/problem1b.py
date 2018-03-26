import networkx as nx
import operator
import timeit
from numpy import linalg as LA
import numpy
import networkx as nx
from random import *
import matplotlib.pyplot as plt
import numpy

print
netsci = nx.read_gml('netscience_component.gml', label='id')

print("this is the average shortest path length")
total_path_length = 0.0
avg_path_length = 0

num_connect_component = nx.number_connected_components(netsci)
num_nodes = nx.number_of_nodes(netsci)
print "number of connected component is ", num_connect_component
print " number of edges is " , nx.number_of_edges(netsci)

def computestat(G, graph_name):
    avg_path_length = nx.average_shortest_path_length(G)
    print "the average path length is ", avg_path_length
    print

    print "the clustering coeff is " , nx.average_clustering(netsci)

    print

    degree_sequence = sorted(nx.degree(G).values(), reverse=True)
    Gdegrees = list(set([(i, degree_sequence.count(i)) for i in degree_sequence]))

    fig = plt.figure()
    ax = plt.gca()
    ax.plot([i[0] for i in Gdegrees],
            [float(i[1]) / (num_nodes) for i in Gdegrees], c='b', linestyle='None', marker='.',
            label='Degree Distribution')

    plt.xlabel("Degree k")
    plt.ylabel('Probabiliy p_k')
    plt.title('Degree Distributions')
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.legend(loc='lower left');

    plt.savefig("problem"+graph_name+" .png")

    plt.show()
    plt.close()



for g in nx.connected_component_subgraphs(netsci):

    if nx.number_of_nodes(g) != 1:
        #print nx.average_shortest_path_length(g)
        total_path_length += nx.average_shortest_path_length(g)



avg_path_length = total_path_length / nx.number_connected_components(netsci)

print "this is the final value of avg path length ", avg_path_length

print

print

print "below is part 2 of part b question 1"

print

print "the average clustering coefficient of netsci is " , nx.average_clustering(netsci)


print " below is the log log plot of the degree distribution "


degree_sequence=sorted(nx.degree(netsci).values(),reverse=True)
Gdegrees=list(set([(i,degree_sequence.count(i)) for i in degree_sequence]))

fig = plt.figure()
ax = plt.gca()
ax.plot([i[0] for i in Gdegrees],
    [float(i[1])/(num_nodes) for i in Gdegrees], c='b', linestyle='None', marker='.', label='Degree Distribution')


plt.xlabel("Degree k")
plt.ylabel('Probabiliy p_k')
plt.title('Degree Distributions')
ax.set_yscale('log')
ax.set_xscale('log')
plt.legend(loc='lower left');
plt.savefig("problem1b.png")
plt.show()
plt.close()




