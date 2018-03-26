import networkx as nx
import operator
import timeit
from numpy import linalg as LA
import numpy

# Calculate modularity for a graph given the components and total number of edges
def modularity(G, comp, m):
    modul = 0
    # treat each component separately
    for nodeset in comp:
        # iterate through all nodes for i and j
        for nodei in list(nodeset):
            for nodej in list(nodeset):
                # if the nodes are neighbors then add one (for Aij)
                if nodei in G.neighbors(nodej):
                    modul = modul+1
                # subtract di*dj/2m
                modul = modul-(G.degree(nodei)*G.degree(nodej)/(2.0*m))
    modul = modul / (2.0 * m)
    #return the modularity score
    return modul

def bbd(G):
    # start a timer
    start = timeit.default_timer()
    # store the total number of edges and nodes
    m = G.number_of_edges()
    n = G.number_of_nodes()

    # get the initial number of connected components
    num_comp = nx.number_connected_components(G)
    # get the initial modularity score
    modcompare = modularity(G, nx.connected_components(G), m)
    print "starting modularity is ", modcompare
    modnew = modcompare
    # create a variable to help exit while loop
    var = True

    while var:
        # set no edges to have been removed
        edgeRemoved = False
        # update the modularity score to compare against for stopping
        modcompare = modnew
        # iterate through all community sub graphs
        for g in list(nx.connected_component_subgraphs(G)):
            # get adjacency matrix as an array with floats
            A = nx.adj_matrix(g).toarray().astype(float)
            L=A

            # create the L matrix
            for nodei in g.nodes():
                for nodej in g.nodes():
                    # for each spot in the matrix, Lij = Dij-Aij where Dij is sum of row/col diagonal matrix
                    if nodei != nodej:
                        L[g.nodes().index(nodei),g.nodes().index(nodej)] =\
                            A[g.nodes().index(nodei),g.nodes().index(nodej)]*(-1)
                    # L = D if no self edges
                    else:
                        L[g.nodes().index(nodei), g.nodes().index(nodej)]=numpy.sum(A[g.nodes().index(nodei),:])
            #find eigen vectors and values                
            w,v = LA.eig(L)
            # get eigen values as a list
            w_list = w.tolist()
            smallest_copy = numpy.argmin(w)
            # sort eigen values
            w_list = sorted(w_list)
            # remove smallest eigen value and store second smallest
            del w_list[0]
            second_small = w_list[0]

            # get the eigen vector for the second smallest eigen value
            second_smallest_index = numpy.where(w==second_small)
            second_smallest_index = second_smallest_index[0][0].item()
            large_eig_vector = v[:, second_smallest_index]

            nodeList = nx.nodes(g)
            # iterate through edges
            for edge in nx.edges(g):
                #if the edge's nodes have different signs in eigen vecotr remove the edge
                source,target = edge
                if large_eig_vector[g.nodes().index(source)]*large_eig_vector[g.nodes().index(target)] < 0:
                    G.remove_edge(source,target)
                    edgeRemoved = True
                    # if removing edge created new component print how many and the modularity score
                    if num_comp < nx.number_connected_components(G):
                        print nx.number_connected_components(G), "is the num of clusters",
                        modcompare = modnew
                        modnew = modularity(G, nx.connected_components(G), m)
                        print modnew, " is the modularity of current split", modcompare
                        # if the modularity score decreased then exit the loop
                        if modnew < modcompare:
                            var = False
                            break
                        num_comp = nx.number_connected_components(G)
            # if no edges are removed exit the loop
            if edgeRemoved == False:
                var = False

    #end timer and print results
    stop = timeit.default_timer()
    print
    print "time to complete was ", stop - start, "seconds"


