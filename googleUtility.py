import googlemaps
from datetime import datetime

# Direction { from: home, to: destinate, time: hour, distance: miles}

#gmaps = googlemaps.Client(key='')

# Request directions via public transit
now = datetime.now()

# validate location function

# calculate distance
class GoogleAPI():
    def __init__(self):
        self.gmaps = googlemaps.Client(key='')

    def directions(self, origin, destination):
        try:
            results = self.gmaps.directions(origin, destination, departure_time=now)
            print(results[0]['legs'][0]['distance']['text'])
            print(results[0]['legs'][0]['duration']['text'])
            print(results[0]['legs'][0]['duration_in_traffic']['text'])
            print(results[0]['legs'][0]['end_address'])
            print(results[0]['legs'][0]['start_address'])
        except:
            sys.exit("Error")
