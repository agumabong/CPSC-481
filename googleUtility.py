import googlemaps, json
from datetime import datetime

# Load config file
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# Direction { from: home, to: destinate, time: hour, distance: miles}
now = datetime.now()

# calculate distance
class GoogleAPI():
    def __init__(self):
        self.gmaps = googlemaps.Client(key=data['apikey'])

    def directions(self, origin, destination):
        try:
            results = self.gmaps.directions(origin, destination, departure_time=now)
            jsonBody = {'start':'','end':'','distance':'','duration':'','duration_traffic':''}
            jsonBody['start'] = results[0]['legs'][0]['start_address']
            jsonBody['end'] = results[0]['legs'][0]['end_address']
            jsonBody['distance'] = results[0]['legs'][0]['distance']['text']
            jsonBody['duration'] = results[0]['legs'][0]['duration']['text']
            jsonBody['duration_traffic'] = results[0]['legs'][0]['duration_in_traffic']['text']
            # print(jsonBody)
            return jsonBody
        except:
            sys.exit("Google API Error")
