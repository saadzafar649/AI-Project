from util import *

def BFS(start, goal, graph = {}, directed=True):
    # moves = len(graph.keys())*80
    # print(main.graph)
    print(start, goal)
    # graph = main.graph if directed else main.graphUnDir
    queue = [start]
    visited = [start]
    parent = {start: start}
    while queue:
        first = queue.pop(0)
        print(first)
        if goal == first:
            return (1, findPath(goal,parent))
        for i in graph[first]:
            if i not in visited:
                parent[i] = first
                queue.append(i)
                visited.append(i)

        # moves -= 1
        # if moves <= 0:
        #     return (0, "Stuck in loop")

    return (0, "Path does not found")
