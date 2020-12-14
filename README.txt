The final algorithm is in "topkmultisourceBFS.py"


Undirected graph data should be in the following format.
-----------------------------------------------------------------------------------------------
# Directed graph (each unordered pair of nodes is saved once): filename.txt 
# Name of road network
# Nodes: 4 Edges: 3
# FromNodeId        ToNodeId
0        1
1        0
1        2
2        1
0        3
3        0
-----------------------------------------------------------------------------------------------


Hospital data should be in the following format(first line contains the number of hospitals h, h lines follow).
-----------------------------------------------------------------------------------------------
# 2
0
2
-----------------------------------------------------------------------------------------------


Save the graph data file and the hospital data file in this directory and run the "driver.py" file. You will
be prompted to enter the filenames of your graph and hospital data. The driver is defaulted to run the final
"topkmultisourceBFS" algorithm with k = 5. Open the driver and change the parameters calling
topKmultisourceBFS(graph1,hospitals,k) to test out different k values.


Nearest hospital data is saved to a file in the following format.
-----------------------------------------------------------------------------------------------
Node: [NodeID]        distance: [distance]        Path: [NodeID]->[intermediateNodeIDs]->[hospitalID]
-----------------------------------------------------------------------------------------------
The data is outputted in increasing NodeID.


Top k nearest hospitals data is saved to a file in the following format.
-----------------------------------------------------------------------------------------------
Node: [NodeID]        distance: [distance]        hospital: [hospitalID]
-----------------------------------------------------------------------------------------------
The data is outputted in increasing NodeID followed by increasing distance.