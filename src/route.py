import requests
import json
import polyline
from geopy.distance import geodesic

import requests


def get_coordinates(location):
    # Construct the request URL
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}'

    # Send the request
    response = requests.get(url)
    data = response.json()

    # Parse the response
    if data['status'] == 'OK':
        # Extract latitude and longitude
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        print(f"Error: {data['status']} - {data.get('error_message', '')}")
        return None, None

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'
location = 'New York'

latitude, longitude = get_coordinates(location, api_key)
if latitude is not None and longitude is not None:
    print(f"Coordinates of {location}: Latitude {latitude}, Longitude {longitude}")


class route():
    def __init__(self, start, dest):

        if type(start) == "str":
            get_coordinates(start)
        if type(start) == "str":
            get_coordinates(dest)
        self.start = start
        self.dest = dest
        # Define the request payload
        payload = {
        "origin": {
            "location": {
            "latLng": {
                "latitude": start[0],
                "longitude": start[1]
            }
            }
        },
        "destination": {
            "location": {
            "latLng": {
                "latitude": dest[0],
                "longitude": dest[1]
            }
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "computeAlternativeRoutes": False,
        "routeModifiers": {
            "avoidTolls": False,
            "avoidHighways": False,
            "avoidFerries": False
        },
        "languageCode": "en-US",
        "units": "METRIC"
        }

        # Define the headers
        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': 'AIzaSyCLTR5jt4ev0PdxstLdqYjuFUxeGnzVq7M',
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
        }

        # Make the request
        self.response_json = requests.post('https://routes.googleapis.com/directions/v2:computeRoutes', json=payload, headers=headers).json()

        self.encoded_polyline = self.response_json['routes'][0]['overview_polyline']['points']
        self.decoded_polyline = polyline.decode(self.encoded_polyline)
    def get_point(self, distance):

        # Initialize variables
        distance_traveled = 0
        last_point = self.decoded_polyline[0]

        # Iterate through the decoded polyline and calculate distance
        for point in self.decoded_polyline[1:]:
            distance_traveled += geodesic(last_point, point).kilometers
            last_point = point
            
            # Check if distance traveled exceeds 100km
            if distance_traveled >= distance:
                return point