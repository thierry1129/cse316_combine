from random import *
import math
import matplotlib.pyplot as plt
import numpy
import numpy.linalg as linalg

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
for val in pdf_val:
    pdf.append(Z*math.pow(val, -1.0*alpha))

# graph data and expected distribution
fig = plt.figure()
ax = plt.gca()
ax.plot(pdf_val, pdf, '', c='r',linestyle='-', label='pdf')
ax.plot(kvalue, p, '.', c='g', linestyle='None', label='empircal distribution')

# initialize new arrays
partc_p=[]
partc_val=[]
# add log of all values for regression
for i in kdist:
    if p[i-1]>0: #Can't take log of 0
        partc_val.append(math.log(float(kvalue[i-1])))
        partc_p.append(math.log(float(p[i-1])))

# Create nump arrays for linear regression
n = len(partc_val)
B=numpy.array(partc_p)
A=numpy.array(([[partc_val[j], 1] for j in range(n)]))
# run linear regression
X=numpy.linalg.lstsq(A,B)[0]
a=X[0]; b=X[1]
# Solve for and output alpha
alpha_empiracle = a*(-1)
print "alpha = ",alpha_empiracle

# Create line showing pdf for alpha just calculated
Z_emp = (alpha_empiracle-1)*math.pow(kmin, alpha_empiracle-1)
pdf_emp=[]
for val in pdf_val:
    pdf_emp.append(Z_emp*math.pow(val, -1.0*alpha_empiracle))

# plot new line
ax.plot(pdf_val, pdf_emp, '', c='b',linestyle='-', label='pdf from empiracal data')

# label and show graph
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('k')
ax.set_ylabel('P(k)')
plt.title('2c')
plt.legend(loc='lower left');
plt.savefig("problem2c.png")
plt.show()