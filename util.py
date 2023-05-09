def findPath(goal, path):
    finalPath = []
    while goal != path[goal]:
        finalPath.append(goal)
        goal = path[goal]
    finalPath.append(goal)
    return list(reversed(finalPath))