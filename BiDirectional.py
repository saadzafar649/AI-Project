
def biDirectionalSearch(graph, start, goal, directed=True):

    from util import findPathBiDir

    f_queue = [start]
    b_queue = [goal]
    f_visited = []
    b_visited = []
    f_parent = {start: start}
    b_parent = {start: start}

    while f_queue and b_queue:

        first = f_queue.pop(0)
        f_visited.append(first)

        if first in b_visited:
            print(f_parent, b_parent)
            return (1, findPathBiDir(f_parent, b_parent, first, start, goal))

        for i in graph[first]:
            if i not in f_visited:
                f_parent[i] = first
                f_queue.append(i)

        first = b_queue.pop(0)
        b_visited.append(first)

        if first in f_visited:
            print(f_parent, b_parent)
            return (1, findPathBiDir(f_parent, b_parent, first, start, goal))

        for i in graph[first]:
            if i not in b_visited:
                b_parent[i] = first
                b_queue.append(i)

    return (0, "Path does not found")
