import networkx as nx
import random

def SIRmodel(G, I, beta, delta):
    """input graph G and list of infected nodes I
    also input infection and recovery rates
    and carry out SIR model"""
    # set each node to be succeptible
    nx.set_node_attributes(G, 'status', 'S')
    # infect all initial nodes from input
    for n in I:
        G.node[n]['status'] = 'I'
    
    # set while loop iterator to true
    iter = True
    while iter:
        # initialize list of nodes that become infected and cured
        infect = []
        cure = []
        # iterate through all the nodes
        for n in G.nodes(data=True):
            #If the node is susceptible
            if n[1]['status'] == 'S':
                for m in G.neighbors(n[0]):
                    # decide whether or not to infect it by
                    # checking if its neighbors are infected
                    if G.node[m]['status'] == 'I':
                        if random.random() < beta:
                            # if infected by neighbor, add to infect list
                            # and don't check other neigbors
                            infect.append(n[0])
                            break
            # decide whether or not to cure if infected
            if n[1]['status'] == 'I':
                if random.random() < delta:
                    cure.append(n[0])
        # infect all newly infected nodes
        for n in infect:
            G.node[n]['status'] = 'I'
        # cure all newly recovered nodes
        for n in cure:
            G.node[n]['status'] = 'R'

        # Continue to iterate if there are still infected nodes in graph
        stat = nx.get_node_attributes(G,'status')
        iter = 'I' in stat.values()
    # get whether each nodes is S, I, or R
    final_stat = nx.get_node_attributes(G,'status')
    num_recover = 0
    # a loop to calculate recovered nodes.
    for n, status in final_stat.iteritems():
        if status == 'R':
            num_recover=num_recover+1
    # output the % recovered nodes
    return num_recover*1.0/nx.number_of_nodes(G)
        
