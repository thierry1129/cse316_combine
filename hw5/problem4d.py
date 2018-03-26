import networkx as nx
import problem4a
from random import choice
from scipy import stats
import numpy as np

beta = 0.05
delta = 0.5

jazz = nx.read_edgelist("jazz.txt")
ER = nx.gnm_random_graph(nx.number_of_nodes(jazz),
    nx.number_of_edges(jazz))
PA = nx.barabasi_albert_graph(nx.number_of_nodes(jazz),
    nx.number_of_edges(jazz)/nx.number_of_nodes(jazz))

jazz_ep = 0
jazz_prop_infected = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(jazz,[choice(jazz.nodes())], beta,delta)
    if prop_inf>.5:
        jazz_ep = jazz_ep+1
        jazz_prop_infected.append(prop_inf)

ER_ep = 0
ER_prop_infected = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(ER,[choice(ER.nodes())], beta,delta)
    if prop_inf>.5:
        ER_ep = ER_ep+1
        ER_prop_infected.append(prop_inf)

PA_ep = 0
PA_prop_infected = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(PA,[choice(PA.nodes())], beta,delta)
    if prop_inf>.5:
        PA_ep = PA_ep+1
        PA_prop_infected.append(prop_inf)


print "ER", ER_ep
print "PA", PA_ep
print "jazz", jazz_ep
print
chi2 = stats.chi2_contingency([[ER_ep, 100-ER_ep],[jazz_ep, 100-jazz_ep]])
print "ER vs jazz X = ", chi2[0], "p = ", chi2[1] 
print "ER mean proportion = ", np.mean(ER_prop_infected),
print "jazz mean proportion = ", np.mean(jazz_prop_infected)
mw = stats.mannwhitneyu(ER_prop_infected, jazz_prop_infected)
print "U-statistic = ", mw[0],
print "p = ", mw[1]
print
chi2 = stats.chi2_contingency([[PA_ep, 100-PA_ep],[jazz_ep, 100-jazz_ep]])
print "PA vs jazz X = ", chi2[0], "p = ", chi2[1] 
print "PA mean proportion = ", np.mean(PA_prop_infected),
print "jazz mean proportion = ", np.mean(jazz_prop_infected)
mw = stats.mannwhitneyu(PA_prop_infected, jazz_prop_infected)
print "U-statistic = ", mw[0],
print "p = ", mw[1]