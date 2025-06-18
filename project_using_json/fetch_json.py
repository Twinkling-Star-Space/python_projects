import json

from json_flight import flights


for flight in flights:
    print(flight["flight_name"])
    print(flight["source"])
    print("---------------------------")
    print(flight["destination"])



