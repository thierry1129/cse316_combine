import networkx as nx
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
        distances.append(((root,n),G.node[n]["distance"]))
    return distances

print (shortest_distance("HARV"))