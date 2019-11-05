from googleUtility import GoogleAPI

g = GoogleAPI()
def algo(parentArray):
    if len(parentArray) == 1: #if first node
        loc1 = start #set loc1 to start to check lengths of first level branches
    else:
        loc1 = parentArray[-1] #set loc1 to the last element in parent array

    if len(parentArray) != len(allCities): #if there are still unvisited cities
        min = 99999 #set large number for minimum length
        minLocation = '' #name of child with shortest branch
        for j in generateChildren(parentArray): #every place that is unvisited
            if j == None:
                break
            loc2 = j #set as loc2
            results = g.directions(loc1, loc2) #check length
            length = float(results['distance'][:-3].replace(',', ''))
            if length < min:
                min = length
                minLocation = j #choose the shortest branch from loc1
        parentArray.append(minLocation) #append next node to parent array
        algo(parentArray) #recursive call
    else:
        return


def generateChildren(parentArr):
    print(parentArr)
    print(allCities)
    for i in parentArr:
        if i in allCities:
            allCities.remove(i)
    # childrenArr = allCities
    return allCities #returns list of remaining unvisited places

# loc1 = 'anaheim, ca'
# loc2 = 'fullerton, ca'
# g.directions(loc1, loc2)




# for i in middleCities:
#     parentArr = [start]
#     parentArr.append(i)
#     loc1 = i
#     while len(parentArr) != len(middleCities):
#         for j in generateChildren(parentArr):
#             loc2 = j
#             parentArr.append(j)
#             g.directions(loc1, loc2)
allCities = ['fullerton, ca', 'los angeles, ca', 'san francisco, ca', 'seattle, wa']
start = 'fullerton, ca'
end = 'seattle, wa'
# allCities.remove(start)
# allCities.remove(end)
# middleCities = allCities

print(allCities)
# middleCities.remove(start).remove(end)
# print(middleCities)
# middleCities = middleCities.remove(end)
parentArr = [start]

algo(parentArr)

print(parentArr)
