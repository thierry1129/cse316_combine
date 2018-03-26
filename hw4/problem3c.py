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

def bbc(G):
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
        # iterate through all subgraphs
        for g in list(nx.connected_component_subgraphs(G)):
            # exit the loop if helper variable says to
            if var == False:
                break
            # get adjacency matrix as an array with floats
            A = nx.adj_matrix(g).toarray().astype(float)
            B=A
            # Create the B matrix
            for nodei in g.nodes():
                for nodej in g.nodes():
                    # for each spot in the matrix, calculate Bij=Aij-di*dj/2m
                    B[g.nodes().index(nodei),g.nodes().index(nodej)] =\
                        A[g.nodes().index(nodei),g.nodes().index(nodej)] -\
                        g.degree(nodei)*g.degree(nodej)/(2.0*m)
            # get the eigen values and eigen vectors
            w,v = LA.eig(B)
            # get the index for the largest eigen value
            largest_vec_index = numpy.argmax(w)
            # get the eigen vector corresponding to the largest eigenvalue
            large_eig_vector = v[:, largest_vec_index]

            nodeList = nx.nodes(g)
            # iterate through all edges to see if they need to be removed
            for edge in nx.edges(g):
                # get the nodes for each edge
                source,target = edge
                # if the eigen vector component for the two nodes of an edge have different
                # then remove the edge
                if large_eig_vector[g.nodes().index(source)]*large_eig_vector[g.nodes().index(target)] < 0:
                    G.remove_edge(source,target)
                    edgeRemoved = True
                    # now we have removed the edges, check the components
                    if num_comp != nx.number_connected_components(G):
                        # now there are more components, check the modularity scores
                        modcompare = modnew
                        modnew = modularity(G, nx.connected_components(G), m)
                        # print the modularity score and the number of components
                        print " the modularity score is:", modnew, "modcompare", modcompare,
                        num_comp = nx.number_connected_components(G)
                        print "...now ", num_comp, " components"

                        # if the modularity score decreased then set the while loop helper variable to false
                        if (modnew<modcompare):
                            var = False
                            break
        # if no edges were removed in all subgraphs then exit the code
        if edgeRemoved == False:
            var = False

    # end the timer and print the time taken
    stop = timeit.default_timer()
    print
    print "time to complete was ", stop - start, "seconds"

