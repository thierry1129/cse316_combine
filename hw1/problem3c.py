import csv
import networkx as nx
import operator

# create a new empty graph using networkx
G=nx.Graph()

# process the movie actors data and enter it in the graph
with open("imdb_actors.tsv") as tsv:
    tsv.readline()
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_node(line[0], name = line[1])

with open("imdb_edges.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_edge(line[0], line[1])

# use the algorithm in the book to calculate closeness centrality
Gc = max(nx.connected_component_subgraphs(G), key=len)

# c_centrality = nx.closeness_centrality(Gc)
# c_centrality = sorted(c_centrality.items(), key=operator.itemgetter(1))

# highest_degree = c_centrality[-20:]

# for i in reversed(highest_degree):
#     print(Gc.node[i[0]]['name'])


norm=0.0
closeness_cent={}
l_values=[]
for n in Gc.nodes():
    l=nx.single_source_shortest_path_length(G,n).items()
    ave_length=0
    for path in l:
        ave_length+=float(path[1])/(G.number_of_nodes()-1-0)
    norm+=1/ave_length
    closeness_cent[n]=1/ave_length
    l_values.append(closeness_cent[n])


closeness_cent = sorted(closeness_cent.items(), key=operator.itemgetter(1))


# print out top twenty nodes with highest degree centrality measures.

highest_degree = closeness_cent[-20:]

for i in reversed(highest_degree):
    print(Gc.node[i[0]]['name'])


with open("Output.txt", "w") as text_file:
    text_file.write(highest_degree.toString())

