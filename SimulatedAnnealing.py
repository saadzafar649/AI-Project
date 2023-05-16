import itertools
import math
import random

def path_permutation(graph, start, goal):
    citiesList = list(graph.keys())
    myPermutations = list(itertools.permutations(citiesList))
    allPaths = []
    for perm in myPermutations:
        if perm[0] == start:
            temp = []
            for i in perm:
                if i == goal:
                    temp.append(i)
                    break
                temp.append(i)
            if temp not in allPaths:
                allPaths.append(temp)
    return allPaths

def path_validation(paths, graph):
    valid = True
    filtered_paths=[]
    for i in paths:
        valid = True
        for j in range(len(i)-1):
            if i[j+1] not in graph[i[j]]:
                valid = False
                break

        if valid:
            filtered_paths.append(i)

    return filtered_paths

def path_cost(path, weights):
    cost=0
    for i in range(0, len(path) - 1):
        cost += weights[(path[i], path[i + 1])]
    return cost

def simulated_annealing(start, goal, graph, weights):
    #1. permutation of graph keys and filter the permutations which match with our start and goal
    paths = []
    paths = path_permutation(graph, start, goal)

    #2. further filter to check if the permutation path actually exists or not
    final_paths = path_validation(paths, graph)

    if len(final_paths)==0:
        return (0, "Path does not found")

    if len(final_paths)==1:
        return (1, final_paths[0])

    random.shuffle(final_paths)
    print(final_paths)

    i = 0
    start_temp = 10
    final_temp = 1
    cooling_factor = 7
    shortest_path = final_paths[i]

    while start_temp > final_temp and i < len(final_paths)-1:
        currentCost = path_cost(final_paths[i], weights)
        nextCost = path_cost(final_paths[i+1], weights)

        if nextCost > currentCost:
            if random.uniform(0, 1) < math.exp((currentCost - nextCost) / start_temp):
                shortest_path = final_paths[i + 1]
                #currentCost = path_cost(final_paths[i+1])
        else:
            shortest_path = final_paths[i + 1]
            #currentCost = self.findactualpathvalue(allPaths[i + 1])

        start_temp -= cooling_factor
        i += 1
    return (1, shortest_path)


