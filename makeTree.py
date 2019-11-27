from googleUtility import GoogleAPI
from node import Node

googleapi = GoogleAPI()

def makeTree(n, goal, destinationList):
    plist = n.parents.copy()
    dlist = destinationList.copy()
    name = n.name
    # remove itself from destination list
    if n.name in dlist:
        dlist.remove(n.name)

    # Check the parent list and remove from destination list
    for p in plist:
        if p in dlist:
            dlist.remove(p)
    print("Destination List: "+str(dlist))
    print("Dlist size: "+ str(len(dlist)))

    # if end of branch, add goal
    if len(dlist) == 0:
        print("Added goal")
        n.children.append(goal)
        return 0

    else:

        for d in range(len(dlist)):
            # Call API between current node and dlist[d] = data
            data = googleapi.directions(n.name, dlist[d])
            print(type(data))
            # create child node
            childNode = Node(dlist[d], plist, destinationList, data)
            if n.name not in childNode.parents:
                print("Added parent to list")
                childNode.parents.append(name)
            #print("data: "+str(childNode.data['duration']))
            #print("Current: " + str(childNode.name))
            #print("Parents: " + str(childNode.parents))
            #print("Children: "+ str(childNode.children))
            n.children.append(childNode)
            makeTree(childNode, goal, destinationList)
    return 0

# userInput = ['California', 'Dallas', 'Vegas', 'Seattle', 'New York']
# def main():
#     emptyList = []
#     results = []
#     parents = []
#     destinationList = userInput[:-1].copy()
#     print(destinationList)
#     start = Node(userInput[0], emptyList, destinationList[:-1], results)
#     goal = Node(userInput[-1], emptyList, '', '')
#     makeTree(start, goal, destinationList)

# main()
