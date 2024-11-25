#---------------------------------------------------------------------------------------
# Name: addItemPoints.py
# Purpose: Adds an items points to the DB and provides context for confirmation page
#
# Author: Ryan Gascoigne-Jones, Tom Sturgeon
#---------------------------------------------------------------------------------------

import sqlite3
from datetime import date, datetime, timedelta
from dateutil import parser

from users.models import Profile, History


def isAdd(fragment) -> bool:
    """
    Checks whether the fragment is an Add request
    :param fragment: The value of fragment in URL
        type - str
    :return: True when the fragment is an Add request otherwise false
        type - bool
    """
    if fragment.startswith("Add"):
        return True


def showPts(fragment) -> dict:
    """
    Generates an attributes for when a user clicks Add X Points button
    Splits fragment and returns addPts as points and isAdd as True other than them 2 it returns an
    essentially empty dictionary
    :param fragment: The value of fragment in URL
        type - str
    :return lib: All the values passed to webpage, many are N/A and are unused
        type - dict
    """
    
    # Splits fragment into points and item name
    fragment1 = fragment.split("+")
    #fragmentPts2 = (fragmentPts[1]).split("+")
    points = fragment1[1]
    fragLength = len(fragment1)
    name = ""
    for i in range(4,fragLength):
        name = name + " " + fragment1[i]

    # Library of all values used in django templates
    lib = {
        'title': "Item page",
        'itemName' : name,
        'isAdd' : True,
        'addPts' : points
    }

    return lib


def addPtsHistDB(request, points, itemName) -> None:
    """
    Adds new points to a users score on DB
    :param request: The http request from the html]
        type - HttpRequest
    :param points: points of current object to add to user's score
        type - int
    :param itemName: Item name parsed from url of item page
        type - str
    :return: None
    """

    # Get data from db
    old_scor = Profile.objects.filter(user=request.user).first()

    # If the user has a current score, the new points are added onto the user's current score
    if old_scor:
        old_scor.score = old_scor.score + points
        old_scor.save()
    # If the user doesn't have a current score, it assigns the items points as their score
    else:
        Profile.objects.create(username=request.user, score=points)

    ## Should it add points for each item as well? ##
    # Adds Item Name and date scanned to history table which is ouput on Profile page
    profile = Profile.objects.get(user=request.user)
    history = History.objects.create(name=itemName, userId=profile, score=points)



### Is this still necessary / are we still using rank for profile ###
### Also it doesn't work ###
### Could generate rank when a profile page is loaded instead of storing on DB - YES says Phil ###
def updateRank() -> None:
    """
    Updates rank of users according to scores in Profiles table in users.models
    :return: None
    """

    # Updates rank
    score_li = [score_obj.id for score_obj in Profile.objects.all().order_by('-score')]
    n = 1
    for i in score_li:
        userRank = Profile.objects.get(id=i)
        Profile.userRank = n
        n = n + 1


### Backup (previously working code) taken from Food Scanner views.py item() to clean up ###
# To use if we want to put above code in a external module and func
""" addPtsDB(int(lib['addPts'])) """

# Just in case we need to go back to
""" object = Profile.objects.filter(user=request.user).first()
object.score = object.score + (int(lib['addPts'])) """

# Library of all values used in django templates
"""context = {
    'title': "Item Page",
    'name' : lib['itemName'],
    'ecoRating' : lib['itemEcoR'],
    'energy' : lib['itemEner'],
    'nutri' : lib['itemNutr'],
    'proc' : lib['itemProc'],
    'imageLink' : lib['itemImg'],
    'score' : lib['itemPoints'],
    'isError' : lib['isError'],
    'errorMsg' : lib['errorMsg'],
    'isAdd' : lib['isAdd'],
    'addPts' : lib['addPts'],
}"""

def maxScans(request) -> bool:
    """
    checks you not spamming item scans by checking that only 5 items can be scanned in 5 minutes 
    :param request: The http request from the html]
        type - obj (HttpRequest)
    :return: bool
    """
    #Get current user profile
    curProfile = Profile.objects.get(user=request.user)

    #get profile item history
    history = History.objects.raw(f'SELECT id, date_Added FROM users_history WHERE userId_id = {curProfile.id} ORDER BY date_Added DESC')
    
    if len(history) <5:
        return False
    
    try:
    #converts date into string
        nowLong = str(history[0].date_Added)
        thenLong = str(history[4].date_Added)

        #selects time in format of HH:MM:SS
        now = nowLong[11:19]
        then = thenLong[11:19]

        #Selects date in format of YYYY-MM-DD
        nowDay = nowLong[0:10]
        thenDay = thenLong[0:10]

        #Converts time into a number of seconds
        nowInSec = (int(now[0:2])*60*60) + (int(now[3:5])*60) + (int(now[6:8]))
        thenInSec = (int(then[0:2])*60*60) + (int(then[3:5])*60) + (int(then[6:8]))

        #calculates the difference in seconds
        difInSec = nowInSec - thenInSec

        #converts difference in seconds to difference in minutes
        dif = difInSec / 60

        #checks if its the same day and the difference is greater than 5 min
        if nowDay == thenDay and dif < 5:
            return True
    except:
        return False
