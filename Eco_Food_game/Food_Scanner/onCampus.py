import json
import requests
import geopy.distance

#opens and assigns config file to access settings
with open('../config.json') as json_config:
    config = json.load(json_config)

    """
    Gets users location from Google geolocation API
    Pulls the latitude and longitude data
    return - tuple of (Latitude, Longitude)
    """
def getLocation():
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key='+ config['Geolocation_API_Key']
    try:
        r = requests.post(URL)
    except requests.exceptions.RequestException as e:
        return "Err: Geolocation Failed"
    data = r.json()
    #pulls lat/long from api request
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

    """
    Gets campus location from config and device location from getLocation()
    Uses geopy to calculate difference between the two points in km
    If less than or equal to 0.75km return True, otherwise return false
    """
def isOnCampus():
    """Compares user location to specified campus location
    return true if with 0.75km"""
    try:
        campus = (config['uni_lat'],config['uni_long'])
    except:
        return "Err: campus location not found"
    loc = getLocation()
    dist = geopy.distance.geodesic(campus,loc).km
    if dist<=0.75:
        return True
    else:
        return False
