# Route Calculator
This program utilizes Google Directions API to calculate the best route between destinations. User can select best route by distance or time. Destinations are unlimited (be reasonable).

# Libraries
- Python 3.7
- Python Virtual Environment
- Google Directions API: https://developers.google.com/maps/documentation/directions/start

# Installation
1. Create virtual environment
    `virtualenv env`
2. Obtain Google API Key and create config.json file with API key.
    `{apikey:'abcdefg12350'}`
3. Activate virtual environment
    `source env/bin/activate`
4. Install libraries
    `pip install -r requirements.txt`
5. Run program
    `python app.py`

# Running program
1. Enter `distance` or `time`
2. Enter at least 3 locations
3. Enter `end` finished

# Example Program
```Welcome to Route Calculator!
Find the shortest distance or time? distance
Enter starting location (City, State): los angeles
Add next destination (City, State): fullerton
Add next destination or end: long beach
Add next destination or end: irvine
Add next destination or end: pasadena
Add next destination or end: end
Starting algorithm...
Priority Queue:
	 los angeles to irvine 40.4 miles
	 irvine to pasadena 60.9 miles
	 fullerton to pasadena 36.9 miles
	 irvine to pasadena 60.9 miles
	 long beach to pasadena 33.5 miles
Selected: long beach to pasadena
Current path: ['los angeles', 'fullerton', 'irvine', 'long beach']
Algorithm complete...
User Input: ['los angeles', 'fullerton', 'long beach', 'irvine', 'pasadena']
Path: los angeles -> fullerton -> irvine -> long beach -> pasadena
Total: 108.4 miles```
