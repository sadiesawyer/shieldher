import os
import googlemaps
from backend.schemas import PlaceResult

maps_api_key = ""

map = googlemaps.Client(maps_api_key)

def resource_search(query: str):
    try:
        result = map.places(query)
        parsed_result = []
        for place in result['results']:
            place_details = map.place(place["place_id"])
            parsed_result.append(
                PlaceResult(
                    name=place["name"], 
                    address=place["formatted_address"], 
                    place_id=place["place_id"], 
                    website=place_details["result"]["website"]
                )
            )
            
        return parsed_result
            
            
    except googlemaps.exceptions as e:
        print(f"Google Maps API Call Failed: {e}")