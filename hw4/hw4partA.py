import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy


karate = nx.read_gml('karate.gml', label='id')
print('karate has '+str(nx.number_of_nodes(karate))+' nodes')
print('karate has '+str(nx.number_of_edges(karate))+' edges')
print('karate has '+str(nx.average_shortest_path_length(karate))+' avg path length')
print('karate has '+str(nx.average_clustering(karate))+' avg clustering')
print
dolphins = nx.read_gml('dolphins.gml', label='id')

print 'dolphins has', nx.number_of_nodes(dolphins), 'nodes'
print 'dolphins has',nx.number_of_edges(dolphins), 'edges'
print 'dolphins has',nx.average_shortest_path_length(dolphins), 'avg path length'
print 'dolphins has',nx.average_clustering(dolphins), 'avg clustering'
print
jazz = nx.read_pajek("jazz.net").to_undirected()
jazz = nx.Graph(jazz)
print 'jazz has', nx.number_of_nodes(jazz), 'nodes'
print 'jazz has',nx.number_of_edges(jazz), 'edges'
print 'jazz has',nx.average_shortest_path_length(jazz), 'avg path length'
print 'jazz has',nx.average_clustering(jazz), 'avg clustering'
