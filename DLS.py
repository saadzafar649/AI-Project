from util import *

def DLS(graph,limit,start ,goal, directed=True):
    if limit == 0:
        return (0, "Please Enter the limit")
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
        if len(findPath(first,parent)) <= limit:
            for i in graph[first]:
                if i not in visited:
                    parent[i] = first
                    queue.append(i)
                    visited.append(i)
    return (0, "Path does not found")
