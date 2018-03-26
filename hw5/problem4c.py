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
ER_deg_list = ER.degree(ER.nodes())
ER_I = max(ER_deg_list, key=ER_deg_list.get)
PA = nx.barabasi_albert_graph(nx.number_of_nodes(jazz),
    nx.number_of_edges(jazz)/nx.number_of_nodes(jazz))
PA_deg_list = PA.degree(PA.nodes())
PA_I = max(PA_deg_list, key=PA_deg_list.get)

ER_ep_high = 0
ER_prop_infected_high = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(ER,[ER_I], beta,delta)
    if prop_inf>.5:
        ER_ep_high = ER_ep_high+1
        ER_prop_infected_high.append(prop_inf)

PA_ep_high = 0
PA_prop_infected_high = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(PA,[PA_I], beta,delta)
    if prop_inf>.5:
        PA_ep_high = PA_ep_high+1
        PA_prop_infected_high.append(prop_inf)

ER_ep_rand = 0
ER_prop_infected_rand = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(ER,[choice(ER.nodes())], beta,delta)
    if prop_inf>.5:
        ER_ep_rand = ER_ep_rand+1
        ER_prop_infected_rand.append(prop_inf)

PA_ep_rand = 0
PA_prop_infected_rand = []
for k in range(100):
    prop_inf = problem4a.SIRmodel(PA,[choice(PA.nodes())], beta,delta)
    if prop_inf>.5:
        PA_ep_rand = PA_ep_rand+1
        PA_prop_infected_rand.append(prop_inf)

print "ER_high", ER_ep_high
print "ER_rand", ER_ep_rand
print "PA_high", PA_ep_high
print "PA_rand", PA_ep_rand

print "ER_high mean proportion = ", np.mean(ER_prop_infected_high),
print "ER_rand mean proportion = ", np.mean(ER_prop_infected_rand)

mwER = stats.mannwhitneyu(ER_prop_infected_high, ER_prop_infected_rand)
print "U-statistic = ", mwER[0],
print "p = ", mwER[1]

print "PA_high mean proportion = ", np.mean(PA_prop_infected_high),
print "PA_rand mean proportion = ", np.mean(PA_prop_infected_rand)

mwPA = stats.mannwhitneyu(PA_prop_infected_high, PA_prop_infected_rand)
print "U-statistic = ", mwPA[0],
print "p = ", mwPA[1]