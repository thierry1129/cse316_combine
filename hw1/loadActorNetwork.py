import csv
import networkx as nx

G=nx.Graph()

with open("imdb_actors.tsv") as tsv:
    tsv.readline()
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_node(line[0], name = line[1])

with open("imdb_edges.tsv") as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        G.add_edge(line[0], line[1])