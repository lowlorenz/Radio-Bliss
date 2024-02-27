import requests
import polyline
from geopy.distance import geodesic

from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
google_api_key = os.getenv("GOOGLE")


def get_coordinates(location):
    # distance in km
    # Construct the request URL
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}'

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

class route():
    def __init__(self, start, dest):

        #check for being string
        if type(start) == str:
            start = get_coordinates(start)
        if type(dest) == str:
            dest = get_coordinates(dest)

        self.start = start
        self.dest = dest
        # Define the request payload
        payload = {
        "origin": {
            "location": {
            "latLng": {
                "latitude": f'{start[0]}',
                "longitude": f'{start[1]}'
            }
            }
        },
        "destination": {
            "location": {
            "latLng": {
                "latitude": f'{dest[0]}',
                "longitude": f'{dest[1]}'
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
            'X-Goog-Api-Key': google_api_key,
            'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
        }

        # Make the request
        self.response_json = requests.post('https://routes.googleapis.com/directions/v2:computeRoutes', json=payload, headers=headers).json()
        print(self.response_json)
        self.encoded_polyline = self.response_json['routes'][0]['polyline']['encodedPolyline']
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