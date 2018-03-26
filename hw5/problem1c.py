import csv
import matplotlib.pyplot as plt
import networkx as nx
from random import choice
import random

# this is the function that computes and prints out the stats of different graphs.
def computestat(G, graph_name):
    #calculate average pathlength using built in function
    avg_path_length = nx.average_shortest_path_length(G)
    print "the average path length for "+graph_name+" is ", avg_path_length

    # Calculate averate custering coefficient using built in function
    print "the clustering coeff for "+graph_name+" is " , nx.average_clustering(G)

    # use the function in previous homework to plot the degree distribution
    # get and order degree sequence
    degree_sequence = sorted(nx.degree(G).values(), reverse=True)
    # get number of occurances for each degree
    Gdegrees = list(set([(i, degree_sequence.count(i)) for i in degree_sequence]))
    num_nodes = G.number_of_nodes()

    # plot
    fig = plt.figure()
    ax = plt.gca()
    # plot degree vs probability of degree (number of nodes w degree/total num nodes)
    ax.plot([i[0] for i in Gdegrees],
            [float(i[1]) / (num_nodes) for i in Gdegrees], c='b', linestyle='None', marker='.',
            label='Degree Distribution')

    #add titles and labels
    plt.xlabel("Degree k")
    plt.ylabel('Probabiliy p_k')
    plt.title('Degree Distributions')
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.legend(loc='lower left');

    plt.savefig("problem"+graph_name+" .png")

    plt.show()
    plt.close()



## Erdos-Renyi Random Graph
# given
Number_of_nodes=379
m = 914
# p=14484*2/(5242*(5242-1))

ERgraph=nx.Graph()
# make sure graph is 1 connected component
while nx.number_connected_components(ERgraph)!=1:
    ERgraph = nx.Graph()

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
        # add edge between random nodes
        ERgraph.add_edge(first_node, second_node)



## Small-World Random Network
# use build in function to create graph
Number_of_nodes=379
SWgraph=nx.watts_strogatz_graph(Number_of_nodes,4,0.1)



# below is the comfiguration model
# get degree sequence for model
netsci = nx.read_gml('netscience_component.gml', label='id')
degree_seq = nx.degree(netsci).values()

# initialize graph to avoid multigraph. Ensure only 1 connected component
nx_empty_graph = nx.Graph()
while nx.number_connected_components(nx_empty_graph)!=1:
    nx_empty_graph = nx.Graph()
    # use networkx function
    config = nx.configuration_model(degree_seq, create_using=nx_empty_graph)


# below is the BA mdoel
# code from textbook

N0 = 10
p = 0.6
new_nodes = 369

# create starting graph
BA_graph = nx.gnp_random_graph(N0, p)

# for each new node
for eti in range(new_nodes):
    m = 2
    new_eti = "_" + str(eti)
    target_nodes = []
    while m != 0:
        part_sum = 0.0
        rn = random.random()
        for n in BA_graph.nodes():
            # calculate range based on degree for each node
            base = part_sum
            step = part_sum + BA_graph.degree(n) / (BA_graph.number_of_edges() * 2.0)
            part_sum = part_sum + BA_graph.degree(n) / (BA_graph.number_of_edges() * 2.0)
            # add edge to node if random number falls in the degree
            if rn >= base and rn < step:
                if n in target_nodes: break
                target_nodes.append(n)
                m = m - 1
                break
    # add all edges found above
    for n_tar in target_nodes:
        BA_graph.add_edge(new_eti, n_tar)


# call function created above for each graph
computestat(ERgraph, "ERgraph")
computestat(SWgraph, "SWgraph")
computestat(config, "configGraph")
computestat(BA_graph, "BA_graph")

