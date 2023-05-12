from util import *

def Astar(graph, weights, heuristic, start, goal, directed=True):
    print(start, goal)
    queue = [(0 + heuristic[start], start)]
    visited = []
    parent = {start: start}
    while queue:
        cost, first = queue.pop(0)
        visited.append(first)
        print(first)

        if goal == first:
            print("FOUND")
            return (1, findPath(goal, parent))

        for i in graph[first]:
            second_items = [tup[1] for tup in queue]

            if i not in visited and i not in second_items:
                parent[i] = first
                queue.append((cost + weights[(first, i)] + heuristic[i], i))
            second_items.clear()

        queue.sort()

    return (0, "Path does not found")