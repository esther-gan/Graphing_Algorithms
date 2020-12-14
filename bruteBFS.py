
# Function to print a BFS of graph 
def BFS(graph, hospitals):

    #open file to save output
    outputFile = open("BFSPaths.txt", "w+")
    
    numOfNodes = len(graph.V)

    for src in graph.V:
        if not(src in hospitals):

            # Mark all the vertices as not visited 
            visited = set()
            paths = {}
        
            # Create a queue for BFS 
            queue = [] 
            distance = 0
        
            # Mark the source node as  
            # visited and enqueue it 
            queue.append((src,distance)) 
            visited.add(src)
            canReachHospital = False
        
            while (queue and not canReachHospital): 
        
                # Dequeue a vertex from  
                # queue and print it 
                s, distance = queue.pop(0) 
                distance += 1

                # Get all adjacent vertices of the 
                # dequeued vertex s. If a adjacent 
                # has not been visited, then mark it 
                # visited and enqueue it 
                for i in graph.graph[s]: 
                    if i not in visited:
                        if (i in hospitals):
                            outputFile.write("Node " +  str(src) + ":\t" + "distance: " + str(distance))
                            # write path
                            path = str(i)
                            j = i
                            paths[i]=s
                            while (j != src):
                                j = paths[j]
                                path = str(j) + "->" + path
                            outputFile.write("\tPath: " + path + "\n")
                            canReachHospital = True
                            break
                        else:
                            queue.append((i,distance)) 
                            visited.add(i)
                            paths[i]=s
            
            if (not canReachHospital):
                outputFile.write("Node " + str(src) + " cannot reach any hospital!!\n")
    
    outputFile.close()
                