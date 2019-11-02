from googleUtility import GoogleAPI

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
    return validType

def main():
    routeType = ""
    destination = []
    validType = False
    maxDestinations = 1

    print("Welcome to Route Calculator!")
    while not validType:
        validType = askRouteType()

    # Ask user for destinations. 5 max
    destination.append(input("Enter starting location (City, State): "))
    destination.append(input("Add next destination (City, State): "))
    while maxDestinations <= 3:
        tempDestination = input("Add next destination or end: ")
        if tempDestination.lower() == "end":
            break
        else:
            destination.append(tempDestination)
            maxDestinations += 1
    print(destination)

#googleapi.directions(startLoc, nextLoc)

if __name__ == "__main__":
    main()
