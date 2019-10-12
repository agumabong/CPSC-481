#Variables to track if the user wants to find distance or time
distance = False
time = False
locations = []

#ask the user whether or not they want to find shortest distance or time
user_input = input("Sup, find the shortest distance or time?")
if (user_input.lower() == "distance"):
    distance = True
elif (user_input.lower() == "time"):
    time = True
else:
    print("invalid input, please put time or distance")
    
#preliminary starting location
print("You can choose up to 5 places max.")
destination = input("Enter starting location (Format is City, State)")
print("Location sent: " + destination)
locations.append(destination)
cont = input("Add another location: ")
locations.append(cont)

#loop until the user has no more locations
add_routes = 3
route_finished = False
while (route_finished == False and add_routes > 0):
    print("additional locations remaining: " + str(add_routes))
    cont = input("Add another location: (Press 'q' to quit.)")
    if (cont.lower() == "q"):
        route_finished= True
    else:
        print("location added was: " + cont)
        add_routes -=1
        locations.append(cont)
        #send info to the google API

print("List of locations is: " + str(locations))
