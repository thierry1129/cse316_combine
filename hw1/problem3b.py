import csv
import networkx as nx
import operator
from array import  array
# Create a new empty graph G using networkx
G=nx.Graph()
# process the actor files and put the data in the graph
with open("imdb_actors.tsv") as tsv:
    tsv.readline()
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_node(line[0], name = line[1])

with open("imdb_edges.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_edge(line[0], line[1])

# use the betweeness centrality algorithm from book to calculate betweeness centrality
Gc = max(nx.connected_component_subgraphs(G), key=len)

# b_centrality = nx.betweenness_centrality(Gc)

list_of_nodes=Gc.nodes()
num_of_nodes=Gc.number_of_nodes()
b_centrality={} #we will need this dictionary later on
for i in range(num_of_nodes-1):
    for j in range(i+1,num_of_nodes):
        paths=nx.all_shortest_paths(Gc,source=list_of_nodes[i], \
                                    target=list_of_nodes[j])
        count=0.0
        path_diz={}
        for p in paths:
            #print p
            count+=1.0
            for n in p[1:-1]:
                if not path_diz.has_key(n):
                    path_diz[n]=0.0
                path_diz[n]+=1.0
        for n in path_diz.keys():
            path_diz[n]=path_diz[n]/count
            if not b_centrality.has_key(n):
                b_centrality[n]=0.0
            b_centrality[n]+=path_diz[n]

b_centrality = sorted(b_centrality.items(), key=operator.itemgetter(1))

# find top twenty nodes with the highest betweeness centrality
highest_degree = b_centrality[-20:]
# print the actors with highest betweeness centrality out
for i in reversed(highest_degree):
    print(Gc.node[i[0]]['name'])

with open("Output.txt", "w") as text_file:
    text_file.write(highest_degree.toString())