#float(i.data[routeType[0]][0:-3])
import datetime
from genChildren import *
def min(lst, routetype):
    min = 99999
    minIndex = 0
    data = 0
    for i in range(len(lst)):
        # data = lst[i].data
        # data = float(lst[i].data[routetype][0:-2].replace(",",""))
        if routetype == "distance":
            data = float(lst[i].data[routetype].replace(" mi",""))
        elif routetype == "duration":
            # print(lst[i].data)
            # {'start': '', 'end': '', 'distance': '0.0 mi', 'duration': '0 mins', 'duration_traffic': '0 mins'}
            # [routetype]
            # problem 1: routetype = "time", which isn't in the dictionary
            # problem 2: your [0:-x] is hard coded af; try getting rid of " mins" and " mi" instead of getting the digits
            data = float(lst[i].data[routetype].replace(" mins", ""))
        # if len(lst[i].parents) > 0:
        #     print(lst[i].parents[-1], "to",lst[i].name, data)
        if data < min:
            min = data
            minIndex = i
    #print("minIndex: ", minIndex)
    return minIndex

def algo(startNode, end, routetype, userList):
    #print("start node type:", type(startNode))
    pq = [startNode]
    goal = end
    # path = []
    while len(pq) != 0:
        # #print("pq empty?", len(pq) == 0)
        # listOfPq = ""
        # for i in pq:
        #     listOfPq = listOfPq + " " + i.name
        #print("pq before pop: ", listOfPq)
        popped = pq.pop(min(pq, routetype))
        # popped = pq.pop(0)
        # #print("popped type:", type(popped))
        # if len(popped.parents) > 0:
            #print("popped:", popped.parents[-1], "to", popped.name)
        # #print("pq:", pq)
        # #print("pq length:", len(pq))
        # #print("min function type", type(min(pq, routetype)))
        # if popped.name in path:
        #     path.remove(popped.name)
        #     path.append(popped.name)
        # else:
        #     path.append(popped.name)
        if popped.name == goal.name:
            #print("goal reached")
            #print("goal data", popped.data)
            #print("goal.name", popped.name)
            #print("goal.parents", popped.parents)

            path = popped.parents
            path.append(popped.name)
            pathString = path[0]
            for i in path[1:]:
                pathString = pathString + " -> " + i
            return pathString
        else:
            genChildren(popped, goal, userList)
            for i in popped.children:
                if i.visited == False:
                    i.visited = True
                    pq.append(i)
            popped.examined = True

# def time(self):
#     time = self.time
#     day = time // (24 * 3600)
#     time = time % (24 * 3600)
#     hour = time // 3600
#     time %= 3600
#     minutes = time // 60
