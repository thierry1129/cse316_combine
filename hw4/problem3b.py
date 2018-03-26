import networkx as nx
import operator
import timeit

# a custom created function to compute the modularity score of a graph, use the algorithm we learnt inclass
# which is , to sum up the modularity score of each component of the graph.
# the formula is, Aij - di*dj /2m
# we assume that m is constant, and it is the number of edges of the original graph.
def modularity(G, comp, m):
    modul = 0
    for nodeset in comp:
        for nodei in list(nodeset):
            for nodej in list(nodeset):
                if nodei in G.neighbors(nodej):
                    modul = modul+1
                modul = modul-(G.degree(nodei)*G.degree(nodej)/(2.0*m))
    modul = modul / (2.0 * m)

    return modul                   

# a function to compute the betweenness based clustering
def bbb(G):
    start = timeit.default_timer()

    m = G.number_of_edges()

    num_comp = nx.number_connected_components(G)
    sorted_bc=[1]
    actual_number_components=1
    modcompare = modularity(G, nx.connected_components(G), m)
    print "starting modularity is ", modcompare
    # we used the author's code , and his code is basically just removing all of the edges in the graph until there is none
    # what we did is , keep checking on the number of connected components, whenever there is an increase in connected component,
    # check the modularity score, if the score decreases, then stop the program.
    while not sorted_bc==[]:
        d_edge=nx.edge_betweenness_centrality(G)
        sorted_bc = sorted(d_edge.items(), key=operator.itemgetter(1))
        e=sorted_bc.pop()
        G.remove_edge(*e[0])

        if num_comp != nx.number_connected_components(G):
            # now the connected component number increases, so we need to check the modularity score of the new split
            num_comp=nx.number_connected_components(G)
            modnew = modularity(G, nx.connected_components(G), m)
            print " the modularity score is:",modnew,
            print "...now ",num_comp," components"
            if modnew < modcompare:
                break
                # break out the program when the new modularity is smaller, indicating the split before is better than the split now
            modcompare = modnew

        if num_comp>actual_number_components:
            actual_number_components=num_comp

    stop = timeit.default_timer()
    print
    print "time to complete was ", stop-start, "seconds"
