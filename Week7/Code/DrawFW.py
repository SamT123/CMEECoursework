""" Script drawing randomly generated food web. Node size represents body size, edge represents feeding interaction. """

__appname__ = 'DrawFW.py'
__author__  = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports

import networkx as nx
import scipy as sc
import matplotlib.pyplot as p

def GenRdmAdjList(N = 2, C = 0.5):
    """
    Generate a random adjacency list.

    PARAMETERS
    ----------
    N : int
        number of nodes
    C : float
        connectivity - the probability that two wandomly selected nodes are conneted by an edge

    RETURNS
    -------
    list
        List of adjacent nodes

    """

    Ids = range(N)
    ALst = []
    for i in Ids:
        if sc.random.uniform(0,1,1) < C:
            Lnk = sc.random.choice(Ids,2).tolist()
            if Lnk[0] != Lnk[1]: #avoid self (e.g., cannibalistic) loops
                ALst.append(Lnk)
    return ALst

MaxN = 30
C = 0.75

# array of lists adjacency list
AdjL = sc.array(GenRdmAdjList(MaxN, C))

# species IDs
Sps = sc.unique(AdjL) # get species ids

# array of sizes
SizRan = ([-10,10]) #use log10 scale
Sizs = sc.random.uniform(SizRan[0],SizRan[1],MaxN)
p.hist(Sizs) #log10 scale
p.hist(10 ** Sizs) #raw scale
NodSizs= 1000 * (Sizs-min(Sizs))/(max(Sizs)-min(Sizs))
p.close('all') # close all open plot objects
f1 = p.figure()

# automatically generate coords
pos = nx.circular_layout(Sps)

# draw graph
G = nx.Graph()
G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL))
nx.draw_networkx(G, pos, node_size = NodSizs)


# save graph
print("Saving food web to ../Results/FoodWeb.pdf")
p.savefig("../Results/FoodWeb.pdf")