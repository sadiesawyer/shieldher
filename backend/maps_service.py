import os #eventually will want API keys as environment vars
import googlemaps
from backend.schemas import PlaceResult
from config import MAPS_API_KEY

map = googlemaps.Client(MAPS_API_KEY) #maps official docs were useless

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