import json
import requests
import geopy.distance
with open('../config.json') as json_config:
    config = json.load(json_config)

def getLocation():
    """Gets users location from Google geolocation API"""
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key='+ config['Geolocation_API_Key']
    r = requests.post(URL)
    data = r.json()

    lat = data['location']['lat']
    lng = data['location']['lng']
    location = (lat,lng)
    return location

def isOnCampus():
    """Compares user location to specified campus location
    return true if with 0.75km"""
    campus = (config['uni_lat'],config['uni_long'])
    loc = getLocation()
    dist = geopy.distance.geodesic(campus,loc).km
    if dist<0.75:
        return True
    else:
        return False
