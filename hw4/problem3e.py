from problem3b import *
import networkx as nx
from problem3c import *
from problem3d import *

print
karate = nx.read_gml('karate.gml', label='id')
print "below is the result for karate part b "
bbb(karate)
print
karate = nx.read_gml('karate.gml', label='id')
print "below is the result for karate part c "
bbc(karate)
print
karate = nx.read_gml('karate.gml', label='id')
print "below is the result for karate part d "
bbd(karate)


print
karate = nx.read_gml('dolphins.gml', label='id')
print "below is the result for dolphins part b "
bbb(karate)
print
karate = nx.read_gml('dolphins.gml', label='id')
print "below is the result for dolphins part c "
bbc(karate)
print
karate = nx.read_gml('dolphins.gml', label='id')
print "below is the result for dolphins part d "
bbd(karate)

print
#jazz = nx.read_pajek("jazz.net").to_undirected()
#jazz = nx.Graph(jazz)

jazz = nx.read_edgelist("jazz.txt")

print " below is the result for jazz part b"
bbb(jazz)

print
jazz = nx.read_edgelist("jazz.txt")

print " below is the result for jazz part c"
bbc(jazz)

print
jazz = nx.read_edgelist("jazz.txt")
print " below is the result for jazz part d"
bbd(jazz)

