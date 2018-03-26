import networkx as nx
from random import *
import matplotlib.pyplot as plt
import math
import numpy
import numpy.linalg as linalg

netsci = nx.read_gml('netscience_component.gml', label='id')

# initialize new arrays
partd_psum=[]
partd_p=[]
partd_val=[]

kval = sorted(nx.degree(netsci).values(), reverse=True)
num_values = nx.number_of_nodes(netsci)

## Get info for degree distribution
kmax = max(kval) #upper pound of degrees
kmin = min(kval)
kdist = {}
# initialize the list
for l in range(kmax):
    kdist[l+1]=0
#add all values to list
for val in kval:
    kdist[val] = kdist[val]+1

# change degree distribution to fraction instead of count
p = []
kvalue = []
for i in kdist:
    p.append(float(kdist[i])/num_values)
    kvalue.append(i)

for i in kdist:
    # Change to ccdf
    partd_psum.append(sum(p[j] for j in range(i-1, len(kdist))))
    # add logs of values to arrays for least squares
    if partd_psum[i-1]>0:
        partd_val.append(math.log(float(kvalue[i-1])))
        partd_p.append(math.log(float(partd_psum[i-1])))


# Create numpy arrays for linear regression
n = len(partd_val)
B=numpy.array(partd_p)
A=numpy.array(([[partd_val[j], 1] for j in range(n)]))
# run linear regression
X=numpy.linalg.lstsq(A,B)[0]
a=X[0]; b=X[1]
# solve for alpha and output
alpha_d = 1-a
print "alpha = ",alpha_d

# Create line showing pdf for alpha just calculated
Z_d = (alpha_d-1)*math.pow(kmin, alpha_d-1)
pdf_d=[]
pdf_val = range(1,100)
for val in pdf_val:
    pdf_d.append(Z_d*math.pow(val, -1.0*alpha_d))

# plot new line
fig = plt.figure()
ax = plt.gca()

degree_sequence=sorted(nx.degree(netsci).values(),reverse=True)
Gdegrees=list(set([(i,degree_sequence.count(i)) for i in degree_sequence]))

ax.plot([i[0] for i in Gdegrees],
    [float(i[1])/(num_values) for i in Gdegrees], c='b', linestyle='None', marker='.', label='Degree Distribution')


ax.plot(pdf_val, pdf_d, '', c='k',linestyle='-', label='pdf from CCDF')


# label and show graph
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('k')
ax.set_ylabel('P(k)')
plt.title('2d')
plt.legend(loc='lower left');
plt.savefig("problem1f.png")
plt.show()