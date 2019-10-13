#Variables to track if the user wants to find distance or time
distance = False
time = False

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
destination = input("Enter starting location (City, State)")
print("Location sent: " + destination)
cont = input("Add another location: ")

#loop until the user has no more locations
route_finished = False
while (route_finished == False):
    cont = input("Add another location: (enter Q to quit)")
    if (cont.lower() == "q"):
        route_finished= True
    else:
        print("Location added was: " + cont)
        #send info to the google API
