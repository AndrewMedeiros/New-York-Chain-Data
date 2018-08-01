import networkx as nx
import json
import glob
import pandas as pd
import matplotlib.pyplot as plt

with open('C:/Users/Admin/Documents/Gerry Mander/Your State/JSON files/rook.json') as rf:
    rook = json.load(rf)

with open('C:/Users/Admin/Documents/Gerry Mander/Your State/JSON files/queen.json') as qf:
    queen = json.load(qf)

# Read graphs into networkx graph objects.
rook = nx.readwrite.json_graph.adjacency_graph(rook)
queen = nx.readwrite.json_graph.adjacency_graph(queen)

# Find if the rook and queen graphs are connected
isRookConnected = nx.is_connected(rook)
isQueenConnected = nx.is_connected(queen)

print("Rook is connected: " + str(isRookConnected))
print("Queen is connected: " + str(isQueenConnected))


# Report edge sizes.
additional_edges = len(queen.edges) - len(rook.edges)
edgesRook = len(rook.edges)
edgesQueen = len(queen.edges)

# Check to see if there are any edges in the rook that aren't in the queen
redges = set(rook.edges)
qedges = set(queen.edges)
bad_edges = "No"

if not redges.issubset(qedges):
    bad_edges = "Yes"

print("Additional edges in queen graph compared to rook graph= " + str(additional_edges))
print("Bad edges: " + str(bad_edges))
print("Rook edge number is: " + str(edgesRook))
print("Queen edge number is: " + str(edgesQueen))



#Now analyze the number of rook and queen nodes
nodeNum = 0
for node in rook.nodes:
    nodeNum += 1
print("Number of nodes in the graph is: " + str(nodeNum))


# #Now make a histogram of the population by VTD (commented out for saving time when running)
# hist = [rook.nodes[node]["POP10"] for node in rook.nodes()]
# plt.hist(hist, bins = 1000)


#Produce the network graphs of VTDs (graphs commented out to save time when running)
state = 36
allFiles = glob.glob("C:/Users/Admin/Documents/GitHub/redistricting/adjacency_matrix_demo/spatial_indexes/"+str(state)+"_*_idx.txt")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
   df = pd.read_csv(file_,index_col=None, header=None)
   list_.append(df)
frame = pd.concat(list_)

df = frame.rename(index=str, columns={0 : "GEOID", 1: "xaxis", 2:"yaxis"})
pos = df.set_index('GEOID').T.to_dict('list')
pos = {str(i) : (pos[i][0], pos[i][1]) for i in pos.keys()}
                     
# plt.figure(figsize = (10,7))
# nx.draw(rook, pos = pos, node_size=0)

# plt.figure(figsize = (10,7))
# nx.draw(queen, pos = pos, node_size=0)


#Now analyze the number of VTDs with 0 population
zeroNum = 0
oneNum = 0

for node in rook.nodes:
    if rook.nodes[node]["POP10"] == 0:
#       print([node])
        zeroNum += 1
    if rook.nodes[node]["POP10"] == 1:
        oneNum += 1
        
print("Number of zero person VTDs is: " + str(zeroNum))
print("Number of one-person VTDs is: " + str(oneNum))


#Now find out how many boundary nodes there are
boundaries = 0
for node in rook.nodes:
    if rook.nodes[node]["boundary_node"] == 1:
        boundaries += 1    
print("Boundary nodes: " + str(boundaries))


