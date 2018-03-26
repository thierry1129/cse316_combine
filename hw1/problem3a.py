import csv
import networkx as nx
import operator
# create a new empty graph using networkx
G=nx.Graph()

#process the movie actors data and enter it in the graph
with open("imdb_actors.tsv") as tsv:
    tsv.readline()
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_node(line[0], name = line[1])

with open("imdb_edges.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_edge(line[0], line[1])

# use the degree centrality computation method from the book to calculate degree centrality
Gc = max(nx.connected_component_subgraphs(G), key=len)

degree_centrality = nx.degree(Gc)
degree_centrality = sorted(degree_centrality.items(), key=operator.itemgetter(1))

# print out the top twenty nodes with the highest degree centrality
highest_degree = degree_centrality[-20:]

for i in reversed(highest_degree):
    print(Gc.node[i[0]]['name'])