def top_k_multisource_bfs(graph, hospitals, k):
    all_distances = {} #{nodeID:[list of k shortest distances]}
    hospital_IDs = {} #{node:[list of k nearest hospitals]}


        
    need_to_visit = {}
    for node in graph.V:
        need_to_visit[node] = k #each node needs to be visited k number of times
        all_distances[node] = []
        hospital_IDs[node] = []
    
    queue = []

    visited = {}
    for h in hospitals:
        visited[h] = set() #each node should be visited at most once, starting from a specific hospital
        visited[h].add(h)
        queue.append((h,0,h))
        need_to_visit[h] -= 1
    
    while (queue):
        node, distance, hosp = queue.pop(0)
        for neighbour in graph.graph[node]:
            if (need_to_visit[neighbour] > 0 and neighbour not in visited[hosp]):
                new_distance = distance + 1
                queue.append((neighbour, new_distance, hosp))
                need_to_visit[neighbour] -= 1
                visited[hosp].add(neighbour)

                if (neighbour not in hospitals):
                    all_distances[neighbour].append(new_distance)
                    hospital_IDs[neighbour].append(hosp)
    
    #open file to save output
    distances_file = open("topKmultisourceDistances.txt", "w+")

    for node in graph.V:
        if node not in hospitals:
            for i in range(0,k):
                try:
                    dist = all_distances[node][i]
                    hosp = hospital_IDs[node][i]
                    distances_file.write("Node " +  str(node) + ":\tdistance: " + str(dist) + "\thospital: " + str(hosp) + "\n")
                except:
                    distances_file.write("Node " +  str(node) + " cannot reach " + str(k) + " hospitals!\n")
                    break

    distances_file.close()
