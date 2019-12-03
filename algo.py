#float(i.data[routeType[0]][0:-3])
from googleUtility import GoogleAPI
from genChildren import *
googleapi = GoogleAPI()

def min(lst, routetype):
    min = 99999
    minIndex = 0
    units = ""
    print("Priority Queue:")
    for i in range(len(lst)):
        # data = lst[i].data

        # print(lst[i].data[routetype], type(lst[i].data[routetype]))
        # data = float(lst[i].data[routetype][0:-2].replace(",",""))
        if routetype == "distance":
            data = float(lst[i].data[routetype][0:-3].replace(",",""))
            units = "miles"
        elif routetype == "duration":
            # tData = lst[i].data[routetype][0:-5].replace(",","")
            # print(tData, type(tData))
            # data = float(tData)
            data = lst[i].data[routetype]
            units = "minutes"
            # print(data, type(data))
            # data = float(tempData[0:-5].replace(",",""))


        if len(lst[i].parents) > 0:
            print("\t", lst[i].parents[-1], "to",lst[i].name, data, units)
        # #print("data type: ", type(data))
        # print("data: ", data)
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
        if len(popped.parents) > 0:
            print("Selected:", popped.parents[-1], "to", popped.name)
            print("Current path:", popped.parents)
        # print("pq:", pq)
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
            total = 0
            path = popped.parents
            path.append(popped.name)
            pathString = path[0]
            for i in path[1:]:
                # total = total + i.data
                units = ""
                loc1 = path[path.index(i)-1]
                loc2 = i
                totalData = googleapi.directions(loc1, loc2)[routetype]
                # print(totalData)
                if routetype == "distance":
                    # print(type(totalData[routetype]))
                    tdata = float(totalData[0:-3].replace(",",""))
                    units = "miles"
                elif routetype == "duration":
                    # tData = lst[i].data[routetype][0:-5].replace(",","")
                    # print(tData, type(tData))
                    # data = float(tData)
                    tdata = totalData
                    units = "minutes"

                total = total + tdata
                pathString = pathString + " -> " + i
            return (pathString, total, units)
        else:
            genChildren(popped, goal, userList[:-1])
            for i in popped.children:
                if i.visited == False:
                    i.visited = True
                    pq.append(i)
            popped.examined = True
