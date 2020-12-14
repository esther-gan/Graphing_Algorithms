def multisource_bfs(graph, hospitals):
    all_distances = {} #{node:distance}
    paths = {} #path[node] stores the next node to travel to, to get to the hospital using the shortest path

    visited = set()
    queue = []

    for h in hospitals:
        queue.append(h)
        all_distances[h] = 0
        visited.add(h)
        paths[h] = -1
    
    while (queue):
        node = queue.pop(0)
        for neighbour in graph.graph[node]:
            if (neighbour not in visited):
                queue.append(neighbour)
                all_distances[neighbour] = all_distances[node] + 1
                paths[neighbour] = node
                visited.add(neighbour)

    #open file to save output
    distances_file = open("multisourceDistances.txt", "w+")

    paths_file = open("multisourcePaths.txt", "w+")

    for node in graph.V:
        if node not in hospitals:
            try:
                dist = all_distances[node]
                p = paths[node]
                distances_file.write("Node " +  str(node) + ":\t" + "distance: " + str(dist) + "\n")
                paths_file.write("Node " +  str(node) + ":\t" + "distance: " + str(dist))
                paths_file.write("\tPath: " + str(node))
                while (p != -1):
                    paths_file.write("->" + str(p))
                    p = paths[p]
                paths_file.write('\n')
            except:
                distances_file.write("Node " +  str(node) + " cannot reach any hospital!\n")
                paths_file.write("Node " +  str(node) + " cannot reach any hospital!\n")

    distances_file.close()
    paths_file.close()
