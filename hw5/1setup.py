import networkx as nx

G=nx.read_gml('netscience.gml')
Gc = max(nx.connected_component_subgraphs(G), key=len)
Gc = Gc.to_undirected()
print nx.info(Gc)
for edge in Gc.edges():
    Gc.remove_edge(edge[0],edge[1])
    Gc.add_edge(edge[0],edge[1])
print nx.info(Gc)
nx.write_gml(Gc,'netscience_component.gml')