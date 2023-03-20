#-------------------------------------------------------------------------------
# Name:        onCampus.py
# Purpose:     Tests if location is on campus
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------
import json
import requests
from geopy import distance
#import geopy.distance

### Switch to use config files ###
# Opens and assigns config file to access settings
"""with open('Eco_Food_game/config.json') as json_config:
    config = json.load(json_config)"""


    
def getLocation() -> tuple:
    """
    Gets user location from Google geolocation API
    Pulls the latitude and longitude data
    :return: A tuple of the Latitude and Longitude of the user location
        type - tuple
    """
    ### Switch API key use config file instead ###
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + "AIzaSyCN1AwE1eqibnlt3nOcH7Nrr7BmIFtBAW8" #config['Geolocation_API_Key']
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
        return "Err Longitude not found"
    
    location = (lat,lng)
    return location

    
def isOnCampus() -> bool:
    """
    Gets the campus location from config and device location from getLocation()
    Uses geopy to calculate difference between the two points in km
    :return: True if two points are less than or equal to 0.75km otherwise false
        type - bool
    """
    try:
        ### Switch coords use config files ###
        #campus = (config['uni_lat'],config['uni_long'])
        campus = (50.737126,-3.532565)
    except:
        return "Err: campus location not found"
    loc = getLocation()
    dist = distance.geodesic(campus,loc).km
    
    ### Switch 0.75 use config files ###
    # Returns true if the two points are less than or equal to 0.75km otherwise false
    if dist <= 0.75: #config['range_km']:
        return True
    else:
        return True

