# Function to print a BFS of graph 
def kBFS(graph, hospitals, k):

    #open file to save output
    outputFile = open("topKBFSDistances.txt", "w+")
    
    numOfNodes = len(graph.V)

    for src in graph.V:
        if not(src in hospitals):

            # Mark all the vertices as not visited 
            visited = set()
        
            # Create a queue for BFS 
            queue = [] 
            distance = 0
        
            # Mark the source node as  
            # visited and enqueue it 
            queue.append((src, distance)) 
            visited.add(src)
            needToFind = k
        
            while (queue and needToFind>0): 
        
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
                            outputFile.write("Node " +  str(src) + ":\t" + "distance: " + str(distance)+ "\thospital: " + str(i) + "\n")
                            needToFind -= 1
                            if needToFind<= 0:
                                break
                        queue.append((i, distance)) 
                        visited.add(i)
            
            if (needToFind > 0):
                outputFile.write("Node " + str(src) + " cannot reach " + str(k) + " hospitals!!\n")
    
    outputFile.close()