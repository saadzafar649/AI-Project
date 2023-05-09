from util import *


def BestFS(graph, heuristic, start, goal, directed=True):
    print(start, goal)
    queue = [start]
    visited = []
    parent = {start: start}
    while queue:
        first = queue.pop(0)
        visited.append(first)
        print(first)
        if goal == first:
            return (1, visited)
        children = []
        for i in graph[first]:
            if i not in visited:
                parent[i] = first
                children.append((heuristic[i], i))
        if len(children) > 0:
            children.sort()
            queue.append(children[0][1])

    return (0, "Path does not found")
