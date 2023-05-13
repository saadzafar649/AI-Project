def findPath(goal, path):
    finalPath = []
    while goal != path[goal]:
        finalPath.append(goal)
        goal = path[goal]
    finalPath.append(goal)
    return list(reversed(finalPath))


def findPathBiDir(f_parent, b_parent, intersect, start, goal):
    path = [[], []]

    temp = intersect
    while temp != start:
        path[0].append(temp)
        temp = f_parent[temp]

    path[0].append(temp)
    path[0].reverse()
    if path[0][0] == start and path[0][len(path[0])-1] == goal:
        return path[0]
    temp = b_parent[intersect]
    while temp != goal:
        path[1].append(temp)
        temp = b_parent[temp]

    path[1].append(temp)

    path[0].extend(path[1])
    print(path)
    return path[0]