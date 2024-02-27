import requests
import polyline
from geopy.distance import geodesic
from functools import lru_cache

from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
google_api_key = os.getenv("GOOGLE")


@lru_cache(maxsize=128)
def get_coordinates(location):
    # distance in km
    # Construct the request URL
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}"

    # Send the request
    response = requests.get(url)
    data = response.json()

    # Parse the response
    if data["status"] == "OK":
        # Extract latitude and longitude
        location = data["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return {"lat": latitude, "long": longitude}
    else:
        print(f"Error: {data['status']} - {data.get('error_message', '')}")
        return {"lat": None, "long": None}

def get_route(start, dest):
    # check for being string
    if type(start) == str:
        start = get_coordinates(start)
    if type(dest) == str:
        dest = get_coordinates(dest)
    # Define the request payload
    payload = {
        "origin": {
            "location": {
                "latLng": {"latitude": f"{start['lat']}", "longitude": f"{start['long']}"}
            }
        },
        "destination": {
            "location": {
                "latLng": {"latitude": f"{dest['lat']}", "longitude": f"{dest['long']}"}
            }
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "computeAlternativeRoutes": False,
        "routeModifiers": {
            "avoidTolls": False,
            "avoidHighways": False,
            "avoidFerries": False,
        },
        "languageCode": "en-US",
        "units": "METRIC",
    }

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": google_api_key,
        "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline",
    }

    # Make the request
    response_json = requests.post(
        "https://routes.googleapis.com/directions/v2:computeRoutes",
        json=payload,
        headers=headers,
    ).json()

    print(response_json)

    overall_distance = response_json["routes"][0]["distanceMeters"] / 1000
    encoded_polyline = response_json["routes"][0]["polyline"]["encodedPolyline"]
    decoded_polyline = polyline.decode(encoded_polyline)
    return decoded_polyline, overall_distance

def get_point(polyline, frac_distance, overall_distance):

    # from 0 to 1

    assert frac_distance <= 1.0 and frac_distance >= 0
    distance = overall_distance*frac_distance

    # Initialize variables
    distance_traveled = 0
    last_point = polyline[0]

    # Iterate through the decoded polyline and calculate distance
    for point in polyline[1:]:
        distance_traveled += geodesic(last_point, point).kilometers
        last_point = point

        # Check if distance traveled exceeds 100km
        if distance_traveled >= distance:
            return point
