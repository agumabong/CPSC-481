from googleUtility import GoogleAPI
from makeTree import *

googleapi = GoogleAPI()

def askRouteType():
    user_input = input("Find the shortest distance or time? ")
    if (user_input.lower() == "distance"):
        routeType = "distance"
        validType = True
    elif (user_input.lower() == "time"):
        routeType = "time"
        validType = True
    else:
        print("Invalid input, please put time or distance")
        validType = False
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
    print(userInput)

    # make tree
    emptyList = []
    emptyDict = {}
    parents = []
    destinationList = userInput[:-1].copy()
    print(destinationList)
    start = Node(userInput[0], emptyList, destinationList[:-1], emptyDict)
    goal = Node(userInput[-1], emptyList, '', emptyDict)
    makeTree(start, goal, destinationList)

    # accessing nodes
    print(routeType[0])
    #print(start.destinations)
    #print(start.children)
    for child in start.children:
        print(child.data['distance'])

    # get data['distance']
    # use start node

#googleapi.directions(startLoc, nextLoc)

if __name__ == "__main__":
    main()
