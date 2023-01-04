import googlemaps
from datetime import datetime
import os
import sys

def find_route(DESTINATION, directionBlob, type="BEST_ROUTE"):
  route=""
  total_duration=0
  for step in directionBlob[0]['legs'][0]['steps']:
    total_duration+=int(step['duration']['text'].split(" ", 1)[0])
    if(step['travel_mode']) == 'TRANSIT':
      transit=step['transit_details']
      TRAVEL_MODE=f"{transit['line']['short_name']} | {step['html_instructions']} | Stops: {transit['num_stops']} | Stop At: {transit['arrival_stop']['name']} | "
    else:
      TRAVEL_MODE=step['html_instructions']
    route+=f"{TRAVEL_MODE}({step['duration']['text']}) --->\n\t\t"

  print(f"DESTINATION:\t{DESTINATION}\n{type}: \t{route} == {total_duration} mins\n")

gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_API_KEY'])

# Request directions via public transit
START_ADDRESS=sys.argv[1]
DESTINATION_LIST=["Delivery Hero SE, Oranienburger Straße, Berlin","Alexanderplatz Berlin","Berlin Zoological Garden, Hardenbergpl. 8, 10787 Berlin"]

print(f"START_ADDRESS: {START_ADDRESS}\n\n")
now = datetime.now()

for dest in DESTINATION_LIST:
  direction_bestroute_result = gmaps.directions(START_ADDRESS,dest,mode="transit",departure_time=now)
  find_route(dest, direction_bestroute_result)
  direction_lesswalking_result = gmaps.directions(START_ADDRESS,dest,mode="transit",transit_routing_preference="less_walking",departure_time=now)
  find_route(dest, direction_lesswalking_result, "LESS_WALKING")
  print("===================================================================================================")
