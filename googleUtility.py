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
            print(results[0]['legs'][0]['distance']['text'])
            print(results[0]['legs'][0]['duration']['text'])
            print(results[0]['legs'][0]['duration_in_traffic']['text'])
            print(results[0]['legs'][0]['end_address'])
            print(results[0]['legs'][0]['start_address'])
        except:
            sys.exit("Google API Error")
