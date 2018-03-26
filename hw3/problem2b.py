from random import *
import math
import matplotlib.pyplot as plt

# Given Values
kmin = 1
alpha = 3.0
num_values=50000
# Derived in question 1a
Z = (alpha-1)*math.pow(kmin, alpha-1)

# use samplig technique from 2a 50000 times
kval = [];
for l in range(0,num_values):
    u = random()
    k = kmin*math.pow(u,(1/(1-alpha)))
    k = int(round(k))
    kval.append(k)

## Get info for degree distribution
kmax = max(kval) #upper pound of degrees
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

# Powerlaw expected pdf values for k<1000
pdf_val = range(1,1000)
pdf = []
for val in pdf_val: #from normalized pdf in question 1
    pdf.append(Z*math.pow(val, -1.0*alpha))

# graph data and expected distribution
fig = plt.figure()
ax = plt.gca()
ax.plot(pdf_val, pdf, '', c='r',linestyle='-', label='pdf')
ax.plot(kvalue, p, '.', c='g', linestyle='None', label='empircal distribution')

# Correct access and labels
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('k')
ax.set_ylabel('P(k)')
plt.legend(loc='lower left');
plt.title('2b')
plt.savefig("problem2b.png")
plt.show()