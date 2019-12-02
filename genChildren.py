from googleUtility import GoogleAPI
from node import Node
import random

googleapi = GoogleAPI()

def genChildren(n, goal, destinationList):
    plist = n.parents.copy()
    dlist = destinationList.copy()
    name = n.name
    if n.name in dlist:
        dlist.remove(n.name)

    # Check the parent list and remove from destination list
    for p in plist:
        if p in dlist:
            dlist.remove(p)
    #print("Destination List: "+str(dlist))
    #print("Dlist size: "+ str(len(dlist)))
    # print(dlist)
    if len(dlist) == 0:
        #print("added goal")

        data = googleapi.directions(n.name, goal.name)
        newGoal = Node(goal.name, [], [], data)
        # #print("goal parents", goal.parents)
        # #print("n.parents", n.parents)
        # #print("n.name", n.name)
        # goal.parents.clear()
        for i in n.parents:
            newGoal.parents.append(i)
        newGoal.parents.append(n.name)
        #     goal.parents.append(i)
        # goal.parents.append(n.name)

        # print("new goal parents:", newGoal.parents)
        # goal.parents.append(n.parents)
        # goal.parents.append(name)
        # n.children.append(goal)
        n.children.append(newGoal)
        return 0

    else:

        for d in range(len(dlist)):
            # Call API between current node and dlist[d] = data
            data = googleapi.directions(n.name, dlist[d])
            # data = random.randint(0,50)
            #print("rand data: ", data)
            childNode = Node(dlist[d], plist, destinationList, data)
            #print("data in node: ", childNode.data)
            if n.name not in childNode.parents:
                #print("added parent to list")
                childNode.parents.append(name)
            # print("Current: " + str(childNode.name))
            # print("Parents: " + str(childNode.parents))
            # print("Children: "+ str(childNode.children))
            n.children.append(childNode)
            # makeTree(childNode, goal, destinationList)
    return 0

# userInput = ['California', 'Dallas', 'Vegas', 'Seattle', 'New York']
# def main():
#     emptyList = []
#     results = []
#     parents = []
#     destinationList = userInput[:-1].copy()
#     #print(destinationList)
#     start = Node(userInput[0], emptyList, destinationList[:-1], results)
#     goal = Node(userInput[-1], emptyList, '', '')
#     makeTree(start, goal, destinationList)

# main()
