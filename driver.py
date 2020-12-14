from bruteBFS import BFS as bruteBFS
from topKBFS import kBFS as topKBFS
from multisourceBFS import multisource_bfs as multisourceBFS
from topKmultisourceBFS import top_k_multisource_bfs as topKmultisourceBFS
from datetime import datetime

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
    # Constructor 
    def __init__(self, vertices): 
        self.V = set()
        self.graph = {}
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        if u in self.V:
            self.graph[u].append(v) 
        else:
            self.graph[u] = [v]
            self.V.add(u)

graph1 = None
hospitals = set() #set of all hospitals

graph_path = input("Path to file1.txt: ")
#for file1, the whole graph 
with open(graph_path, "r") as f:
    #get number of nodes from txt, nodes = xxx
    graph_list = f.readlines()
    info_line = graph_list[2]
    info_line = info_line.split()
    info = []
    for i in info_line:
        if i.isdigit():
            info.append(i)

    graph1 = Graph(int(info[0]))

    for line in graph_list[4:]:
        line_int = line.split()
        loc1 = int(line_int[0])
        loc2 = int(line_int[1])
        graph1.addEdge(loc1, loc2)

#for file2, the nodes that are hospitals
hospital_path = input("Path to file2.txt: ")
with open(hospital_path, "r") as f:
    hospital_list = f.readlines()
    # remove header
    hospital_list = hospital_list[1:]
    for line in hospital_list:
        hospitals.add(int(line))

start = datetime.now()
print("start = " + str(start))
#bruteBFS(graph1,hospitals)
#multisourceBFS(graph1,hospitals)
#topKBFS(graph1,hospitals, 5)
topKmultisourceBFS(graph1,hospitals, 5)
end = datetime.now()
print("end = " + str(end))
diff = end - start
print("time taken = " + str(diff.total_seconds()))


