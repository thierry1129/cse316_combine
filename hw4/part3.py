import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy
import operator


karate = nx.read_gml('karate.gml', label='id')

nx.adj_matrix