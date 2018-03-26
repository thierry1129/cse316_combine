from random import *
import math
import matplotlib.pyplot as plt
import numpy
import numpy.linalg as linalg


partd_alpha=[]
partc_alpha=[]
for m in range(100):
    kmin = 1
    alpha = 3.0
    num_values=50000

    kval = [];

    for l in range(0,num_values):
        u = random()
        k = kmin*math.pow(u,(1/(1-alpha)))
        k = int(round(k))
        kval.append(k)

    kmax = max(kval)
    kdist = {}
    for l in range(kmax):
        kdist[l+1]=0
    for val in kval:
        kdist[val] = kdist[val]+1

    p = []
    kvalue = []
    for i in kdist:
        p.append(float(kdist[i])/num_values)
        kvalue.append(i)


    pdf_val = range(1,1000)



    partc_p=[]
    partc_val=[]
    # print(kdist)
    # print(p)
    for i in kdist:
        if p[i-1]>0:
            partc_val.append(math.log(float(kvalue[i-1])))
            partc_p.append(math.log(float(p[i-1])))

    n = len(partc_val)
    B=numpy.array(partc_p)
    A=numpy.array(([[partc_val[j], 1] for j in range(n)]))
    X=numpy.linalg.lstsq(A,B)[0]
    a=X[0]; b=X[1]
    alpha_empiracle = a*(-1)
    partc_alpha.append(alpha_empiracle)



    partd_psum=[]
    partd_p=[]
    partd_val=[]

    for i in kdist:
        partd_psum.append(sum(p[j] for j in range(i-1, len(kdist))))
        if partd_psum[i-1]>0:
            partd_val.append(math.log(float(kvalue[i-1])))
            partd_p.append(math.log(float(partd_psum[i-1])))

    n = len(partd_val)
    B=numpy.array(partd_p)
    A=numpy.array(([[partd_val[j], 1] for j in range(n)]))
    X=numpy.linalg.lstsq(A,B)[0]
    a=X[0]; b=X[1]
    alpha_d = 1-a
    partd_alpha.append(alpha_d)




print "using pdf, average alpha = ",numpy.mean(partc_alpha)
print "using pdf, standard deviation alpha = ",numpy.std(partc_alpha)

print "using ccdf, average alpha = ",numpy.mean(partd_alpha)
print "using ccdf, standard deviation alpha ",numpy.std(partd_alpha)