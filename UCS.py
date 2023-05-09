def uniformCostSearch(self, start, goal):
    costs = {(0, 1): 1, (0, -1): 1, (-1, 0): 2, (-1, 1): 3}
    queue = [{start: 0}]
    visited = [start]
    parentData = {start: ""}
    child = None
    print("Traversal = ", end='')
    while queue:
        node = list(queue.pop(0).keys())[0]
        if node == goal:
            child = node
            break
        print(node, end=' -> ')
        possibleMoves = np.add([(0, -1), (0, 1), (-1, 1), (-1, 0)], node).tolist()
        possibleMoves = list(map(tuple, possibleMoves))
        for i in possibleMoves:
            if self.checkindeces(i) and self.grid[i[0]][i[1]] == '0' and i not in visited:
                coord = (i[0] - node[0], i[1] - node[1])
                parentData[i] = node
                visited.append(i)
                index = 0
                for j in queue:
                    if list(j.values())[0] > costs[coord]:
                        break
                    index += 1
                else:
                    index -= 1
                queue.insert(index, {i: costs[coord]})
    if child is None:
        print("\nPath is not possible because the graph is completely traversed but the goal is not found")
        return

    self.tracePath(parentData, child)
    self.display()