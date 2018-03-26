import networkx as nx
from random import *
import matplotlib.pyplot as plt
import numpy
import math



# N0=5
# p=0.6
# new_nodes=1000

alpha_3 = []
for q in range (100):
    G = nx.barabasi_albert_graph(1000, 3)

    degree_sequence=sorted(nx.degree(G).values(),reverse=True)
    Gdegrees=list(set([(i,degree_sequence.count(i)) for i in degree_sequence]))

    partd_psum=[]
    partd_p=[]
    partd_val=[]
    kvalue = []
    p = []

    Gdegrees = sorted(Gdegrees, key=lambda x: x[0])

    for i in range(len(Gdegrees)):
        kvalue.append(Gdegrees[i][0])
        p.append(float(Gdegrees[i][1])/sum(Gdegrees[k][1] for k in range(len(Gdegrees))))

    for i in range(len(Gdegrees)):
        partd_psum.append(sum(p[j] for j in range(i-1, len(Gdegrees))))
        if partd_psum[i-1]>0 and kvalue[i-1]>0:
            partd_val.append(math.log(float(kvalue[i-1])))
            partd_p.append(math.log(float(partd_psum[i-1])))

    # print kvalue
    # print partd_psum

    n = len(partd_val)
    B=numpy.array(partd_p)
    A=numpy.array(([[partd_val[j], 1] for j in range(n)]))

    X=numpy.linalg.lstsq(A,B)[0]
    a=X[0]; b=X[1]
    alpha_d = 1-a
    alpha_3.append(alpha_d)

print "average alpha = ",numpy.mean(alpha_3)
print "standard deviation alpha = ",numpy.std(alpha_3)
