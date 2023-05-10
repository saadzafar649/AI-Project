from DLS import *

def IDS(graph,start ,goal, directed=True):  # DLS code used in this to search at increasing iteratively depth
    cost=0
    boolCheck = False
    limit=0

    while boolCheck == False:
        output=DLS(graph,limit,start ,goal, directed=True)
        boolCheck=output[0]

        if boolCheck == False:
            print(f"Goal wasn't found at depth={limit} so increasing depth to {limit +1}")
            limit += 1

    print(f"Goal found at depth={limit}")
    return output