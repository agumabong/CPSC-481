from googleUtility import GoogleAPI

googleapi = GoogleAPI()

first = input("Enter location(City, State): ")
second = input("Enter location(City, State): ")

googleapi.directions(first, second)
