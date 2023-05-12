from util import *

def Astar(graph, weights, heuristic, start, goal):
    print(start, goal)
    queue = [(0 + heuristic[start], start)]
    visited = []
    parent = {start: start}
    while queue:
        cost, first = queue.pop(0)
        visited.append(first)
        print(first)

        if goal == first:
            return (1, findPath(goal, parent))

        for i in graph[first]:
            nodes_in_queue = [tup[1] for tup in queue]
            if i not in visited and i not in nodes_in_queue:
                parent[i] = first
                queue.append((cost + weights[(first, i)] + heuristic[i], i))
            nodes_in_queue.clear()
        queue.sort()

    return (0, "Path does not found")