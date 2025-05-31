import os #eventually will want API keys as environment vars
import googlemaps
from backend.schemas import PlaceResult

maps_api_key = "" #maps official docs were useless

map = googlemaps.Client(maps_api_key)

def resource_search(query: str):
    try:
        result = map.places(query) #https://googlemaps.github.io/google-maps-services-python/docs/index.html#googlemaps.Client.place omg this was so hard to find
        parsed_result = []
        for place in result['results']: #cycle thru all the results found
            place_details = map.place(place["place_id"]) #had to call details to get websites on a specific place
            parsed_result.append( #parse results for just the fields we're looking for
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