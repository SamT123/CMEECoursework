""" Script to make graph for QMEE collaboration network """

import numpy as np
import pandas as pd
import itertools
import networkx as nx
import matplotlib.pylab as p
import math
import matplotlib.patches as mpatches
# load edges and nodes

edges = pd.read_csv("../Data/QMEE_Net_Mat_edges.csv", header=0)
edges.index = edges.columns
nodes = pd.read_csv("../Data/QMEE_Net_Mat_nodes.csv", header=0,index_col=0) 

# adjacency list
AdjL = []
for inst1,inst2 in itertools.product(edges.index, edges.columns):
    if edges.loc[inst1, inst2] > 0:
        AdjL.append((inst1,inst2,edges.loc[inst1, inst2]))


# species list
sps = nodes.index.to_list()



# sizes
sizeL = nodes['Pis']
# colours
conv = {'University':'green','Hosting Partner':'red','Non-Hosting Partners':'blue'}
collist = [conv[ty] for ty in nodes['Type'].to_list()]

red_patch = mpatches.Patch(color='red', label='Hosting Partner')
green_patch = mpatches.Patch(color='green', label='University')
blue_patch = mpatches.Patch(color='blue', label='Non-Hosting Partner')

# 

# edge type



pos = nx.circular_layout(sps)
ws=np.array([])
G = nx.Graph()
G.add_nodes_from(sps)
for l in AdjL:
    G.add_edges_from([(l[0], l[1])])
    ws=np.append(ws,l[2])


NodSizs= 2000 * (1+sizeL-min(sizeL))/(1+max(sizeL)-min(sizeL))
ws =  np.log(5*(0.1+ws-min(ws))/(0.1+max(ws)-min(ws)))

ws = 5*ws/max(ws)
print(ws)



nx.draw_networkx(G, pos, width=ws,node_size= NodSizs,edge_color='grey', arrows = True, node_color=collist)
p.legend(handles=[red_patch,green_patch,blue_patch], loc = [0,0.7])

p.savefig("../results/QMEE.svg", format = "svg")