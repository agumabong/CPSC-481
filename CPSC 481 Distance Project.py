#Variables to track if the user wants to find distance or time
distance = False
time = False
cities = [] #array to hold initial list of cities

#ask the user whether or not they want to find shortest distance or time
user_input = input("Sup, find the shortest distance or time? ")
if (user_input.lower() == "distance"):
    distance = True
elif (user_input.lower() == "time"):
    time = True
else:
    print("invalid input, please put time or distance")

#preliminary starting location
start = input("Enter starting location (Format is City, State) ")
# cities.append(destination) #appends starting city to array of cities
print("Location sent: " + start)
cont = input("Add another location: ")
cities.append(cont) #appends first destination to array of cities


#loop until the user has no more locations
route_finished = False
while (route_finished == False):
    cont = input("Add another location: (enter Q to quit) ")
    if (cont.lower() == "q"):
        route_finished= True
    else:
        cities.append(cont)
        print("location added was: " + cont)
        #send info to the google API

path = start
for i in cities:
    path = path + " -> " + i

print(path)
