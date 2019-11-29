#float(i.data[routeType[0]][0:-3])
def min(lst, routetype):
    min = 99999
    minIndex = 0
    for i in range(len(lst)):
        # data = lst[i].data
        data = float(lst[i].data[routetype][0:-3].replace(",",""))
        # if routetype == "distance":
        #     data = float(lst[i].data[routetype][0:-3].replace(",",""))
        # elif routetype == "time":
        #     totalTime = 0
        #     time = lst[i].data[routetype]
        #     if day in time:
        #         dayInMins =
        #     data = float(lst[i].data[routetype][0:-5].replace(",",))
        print("data type: ", type(data))
        print("data: ", data)
        if data < min:
            min = data
            minIndex = i
    print("minIndex: ", minIndex)
    return minIndex

def algo(startNode, end, routetype):
    print("start node type:", type(startNode))
    pq = [startNode]
    goal = end
    # path = []
    while len(pq) != 0:
        # print("pq empty?", len(pq) == 0)
        popped = pq.pop(min(pq, routetype))
        # popped = pq.pop(0)
        # print("popped type:", type(popped))
        print("popped:", popped.name)
        # print("pq:", pq)
        # print("pq length:", len(pq))
        # print("min function type", type(min(pq, routetype)))
        # if popped.name in path:
        #     path.remove(popped.name)
        #     path.append(popped.name)
        # else:
        #     path.append(popped.name)
        if popped.name == goal.name:
            print("goal reached")
            print("goal.name", popped.name)
            print("goal.parents", popped.parents)
            path = popped.parents
            path.append(popped.name)
            return path
        else:
            for i in popped.children:
                if i.visited == False:
                    i.visited = True
                    pq.append(i)
            popped.examined = True
