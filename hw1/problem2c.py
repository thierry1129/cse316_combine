import networkx as nx
import matplotlib.pyplot as mp
#generate an empty graph
G=nx.Graph()

#define the nodes from the Arpanet
G.add_nodes_from(['UCSB', 'SRI', 'STAN', 'UCLA', 'UTAH', 'SDC',
    'RAND', 'MIT', 'BBN', 'LINC', 'CASE', 'CARN', 'HARV'])

#add edges
G.add_edges_from([('CASE', 'LINC'),('CASE','CARN'),('CARN', 'HARV'),
    ('HARV','BBN'),('BBN','MIT'),('MIT','LINC'),('MIT','UTAH'),
    ('UTAH','SDC'),('RAND', 'SDC'),('RAND','BBN'),('UTAH','SRI'),
    ('SRI', 'STAN'), ('STAN','UCLA'),('UCLA','RAND'),('SRI','UCLA'),
    ('SRI','UCSB'),('UCSB','UCLA')])

def shortest_distance(root):
    # Below code is from DSCN pg 21
    # Set the root node as root
    root_node=root
    # Add root node to queue
    queue=[]
    queue.append(root)
    # Set the distance of root = 0
    G.node[root]["distance"]=0
    # if the queue is not empty
    while len(queue):
        # take top node from que
        working_node=queue.pop(0)
        # for each neighbor of current node
        for n in G.neighbors(working_node):
            if len(G.node[n])==0:
                G.node[n]["distance"]=G.node[working_node]["distance"]+1
                queue.append(n)
    distances = []
    for n in G.nodes():
        distances.append((sorted([root,n]),G.node[n]["distance"]))
    return distances

locations = ['UCSB', 'SRI', 'STAN', 'UCLA', 'UTAH', 'SDC',
    'RAND', 'MIT', 'BBN', 'LINC', 'CASE', 'CARN', 'HARV']

global_distances = []
distance_locs = []

# use each location as root node
for location in locations:
    #find the shortest distance to every other node
    distances = shortest_distance(location)
    for distance in distances:
        #if the distance has not already been added to the global list
            #add to distance to list and locations to separate list
        if distance[0] not in distance_locs:
            if distance[1]!=0:
                global_distances.append(distance[1])
                distance_locs.append(distance[0])
#make histogram of distance
mp.hist(global_distances,bins=[0,1,2,3,4,5,6], align='left')
#show histogram
mp.show()
#print(global_distances)