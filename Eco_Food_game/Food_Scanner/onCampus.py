#-------------------------------------------------------------------------------
# Name:        onCampus.py
# Purpose:     Tests if location is on campus
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------
import json
import requests
import geopy.distance

# Opens and assigns config file to access settings
with open('../config.json') as json_config:
    config = json.load(json_config)

    
def getLocation() -> tuple:
    """
    Gets user location from Google geolocation API
    Pulls the latitude and longitude data
    @return A tuple of the Latitude and Longitude of the user location
        type - tuple
    """
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + config['Geolocation_API_Key']
    try:
        # Gets the geolocation data of the user from the Google api
        r = requests.post(URL)
    except requests.exceptions.RequestException as e:
        return "Err: Geolocation Failed"
    data = r.json()
    
    # Pulls lat/long from api request
    try:
        lat = data['location']['lat']
    except:
        return "Err: latitude not found"
    try:
        lng = data['location']['lng']
    except:
        return "ErrL Longitude not found"
    
    location = (lat,lng)
    return location

    
def isOnCampus() -> bool:
    """
    Gets the campus location from config and device location from getLocation()
    Uses geopy to calculate difference between the two points in km
    @return True if two points are less than or equal to 0.75km otherwise false
        type - bool
    """
    try:
        campus = (config['uni_lat'],config['uni_long'])
    except:
        return "Err: campus location not found"
    loc = getLocation()
    dist = geopy.distance.geodesic(campus,loc).km
    
    # Returns true if the two points are less than or equal to 0.75km otherwise false
    if dist <= 0.75:
        return True
    else:
        return False
