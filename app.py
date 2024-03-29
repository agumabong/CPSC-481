from googleUtility import GoogleAPI
# from makeTree import *
from algo import *
googleapi = GoogleAPI()

def askRouteType():
    user_input = input("Find the shortest distance or time? ")
    if (user_input.lower() == "distance"):
        routeType = "distance"
        validType = True
    elif (user_input.lower() == "time"):
        routeType = "duration"
        validType = True
    else:
        print("Invalid input, please put time or distance")
        validType = False
        askRouteType()
    return [routeType, validType]

def main():
    userInput = []
    routeType = ["", False]
    maxDestinations = 1

    print("Welcome to Route Calculator!")
    while not routeType[1]:
        routeType = askRouteType()

    # Ask user for destinations. 5 max
    userInput.append(input("Enter starting location (City, State): "))
    userInput.append(input("Add next destination (City, State): "))
    while maxDestinations <= 3:
        tempDestination = input("Add next destination or end: ")
        if tempDestination.lower() == "end":
            break
        else:
            userInput.append(tempDestination)
            maxDestinations += 1
    #print(userInput)

    # make tree
    emptyList = []
    emptyDict = {}
    parents = []
    destinationList = userInput[:-1].copy()
    #print(destinationList)

    # startData = googleapi.directions(userInput[0], userInput[0])
    startData = {'start': '', 'end': '', 'distance': '0.0 mi', 'duration': 0, 'duration_traffic': '0 mins'}
    start = Node(userInput[0], emptyList, destinationList[:-1], startData)
    goal = Node(userInput[-1], emptyList, '', emptyList)
    # print("Generating tree...")
    # makeTree(start, goal, destinationList)

    # accessing nodes
    #print(routeType[0])
    #print("start:", start.name)
    #print(start.destinations)
    # for i in start.children:
        #print(i.name)
        #print(type(i.data))
        #print("data:", i.data)
    # #print(start.children[0].name)
    #print(start.parents)
    # use start node

    # print("========================== START OF ALGORITHM =============================")
    print("Starting algorithm...")
    path = algo(start, goal, routeType[0], userInput)
    print("Algorithm complete...")
    print("User Input:", userInput)
    #print("path type:", type(path))
    print("Path:", path[0])
    print("Total:", path[1], path[2])
#googleapi.directions(startLoc, nextLoc)

if __name__ == "__main__":
    main()
