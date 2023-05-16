import copy
import math


def generateChilds(path, graph):
    lastNode = path[len(path) - 1]
    children = []
    for i in graph[lastNode]:
        if i not in path:
            pathcopy = copy.deepcopy(path)
            pathcopy.append(i)
            children.append(pathcopy)
    print(children)
    return children


def calculateValue(path, weights):
    totalweight = 0
    for i in range(0, len(path) - 1):
        totalweight += weights[(path[i], path[i + 1])]
    return totalweight


def alphaBetaPruninghelper(path, goal, graph, weights, ismin=True, alpha=-math.inf, beta=math.inf):
    if path[len(path) - 1] == goal:
        print(path, calculateValue(path, weights))
        return path, calculateValue(path, weights)

    children = generateChilds(path, graph)
    values = []
    paths = []
    if len(children) == 0:
        if ismin:
            return path, math.inf
        return path, 0

    for i in children:
        path2, value2 = alphaBetaPruninghelper(i, goal, graph, weights, not ismin, alpha, beta)
        if ismin:
            if value2 <= alpha:  # Adjusted the condition to include equality
                return path2, value2
            beta = min(beta, value2)
        else:
            if value2 >= beta:  # Adjusted the condition to include equality
                return path2, value2
            alpha = max(alpha, value2)
        paths.append(path2)
        values.append(value2)

    if ismin:
        index = values.index(min(values))
        return paths[index], values[index]

    index = values.index(max(values))
    return paths[index], values[index]

def alphaBetaPruning(start, goal, graph, weights, ismin=True, alpha=-math.inf, beta=math.inf):
    return (1, alphaBetaPruninghelper([start], goal, graph, weights)[0])