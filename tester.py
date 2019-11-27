import json

jsonBody = {'start':'','end':'','distance':'','duration':'','duration_traffic':''}
jsonBody['start'] = "Los Angeles"
jsonBody['end'] = "New York"
jsonBody['distance'] = "12.3 mi"
jsonBody['duration'] = "23 hours"

def testerFunc(jsonBody):
    print(type(jsonBody))

testerFunc(jsonBody)
