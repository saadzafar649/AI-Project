def findPath(goal, path):
    finalPath = []
    while goal != path[goal]:
        finalPath.append(goal)
        goal = path[goal]
    finalPath.append(goal)
    return list(reversed(finalPath))

def DFS(start, goal, graph, directed=True):
    # print(main.graph)
    print(start, goal)
    # graph = main.graph if directed else main.graphUnDir
    queue = [start]
    visited = [start]
    parent = {start: start}
    while queue:
        first = queue.pop()
        print(first)
        if goal == first:
            return (1, findPath(goal,parent))
        for i in graph[first]:
            if i not in visited:
                parent[i] = first
                queue.append(i)
                visited.append(i)
    return (0, "Path does not found")
