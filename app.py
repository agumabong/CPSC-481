from googleUtility import GoogleAPI

#Variables to track if the user wants to find distance or time
distance = False
time = False
googleapi = GoogleAPI()

#ask the user whether or not they want to find shortest distance or time
print("Welcome to Route Calculator!")
user_input = input("Find the shortest distance or time? ")
if (user_input.lower() == "distance"):
    distance = True
elif (user_input.lower() == "time"):
    time = True
else:
    print("invalid input, please put time or distance")

#preliminary starting location
startLoc = input("Enter starting location (City, State): ")
endLoc = input("Add destination (City, State): ")

googleapi.directions(startLoc, endLoc)
