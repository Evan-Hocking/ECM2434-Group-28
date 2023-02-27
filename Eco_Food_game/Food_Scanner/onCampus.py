#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      evzy
#
# Created:     27/02/2023
# Copyright:   (c) evzy 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
import requests
import geopy.distance
with open('../config.json') as json_config:
    config = json.load(json_config)

def getLocation():
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key='+ config['Geolocation_API_Key']
    r = requests.post(URL)
    data = r.json()

    lat = data['location']['lat']
    lng = data['location']['lng']
    location = (lat,lng)
    return location

def isOnCampus():
    campus = (config['uni_lat'],config['uni_long'])
    loc = getLocation()
    dist = geopy.distance.geodesic(campus,loc).km
    if dist<0.75:
        return True
