from googleUtility import GoogleAPI

googleapi = GoogleAPI()

first = input("Enter location(City, State): ")
second = input("Enter location(City, State): ")

results = googleapi.directions(first, second)
print(type(results))
print(results['distance'][:-3])
