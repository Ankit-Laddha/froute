import googlemaps
from datetime import datetime
import os
import sys

def find_route(DESTINATION, directionBlob):
  route=""
  total_duration=0
  for step in directionBlob[0]['legs'][0]['steps']:
    total_duration+=int(step['duration']['text'].split(" ", 1)[0])
    if(step['travel_mode']) == 'TRANSIT':
      transit=step['transit_details']
      TRAVEL_MODE=f"[{transit['line']['short_name']}][{transit['headsign']}][Stops: {transit['num_stops']}]"
    else:
      TRAVEL_MODE=step['travel_mode']
    route+=f"{TRAVEL_MODE}({step['duration']['text']}) ---> "

  print(f"DESTINATION: {DESTINATION}\n\t\t{route} == {total_duration} mins\n")

	
gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_API_KEY'])

START_ADDRESS=sys.argv[1]
DESTINATION_LIST=["Delivery Hero SE, Oranienburger Straße, Berlin","Alexanderplatz Berlin","Berlin Zoological Garden, Hardenbergpl. 8, 10787 Berlin"]
now = datetime.now()

for dest in DESTINATION_LIST:
  direction_result = gmaps.directions(START_ADDRESS,dest,mode="transit",departure_time=now)
  find_route(dest, direction_result)

