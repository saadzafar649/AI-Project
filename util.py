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

    temp = b_parent[intersect]
    while temp != goal:
        path[1].append(temp)
        temp = b_parent[temp]

    path[1].append(temp)

    path[0].extend(path[1])
    return path[0]