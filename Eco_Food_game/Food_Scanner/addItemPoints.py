#---------------------------------------------------------------------------------------
# Name: addItemPoints.py
# Purpose: Adds an items points to the DB and provides context for confirmation page
#
# Author: Ryan Gascoigne-Jones
#---------------------------------------------------------------------------------------
import sqlite3
from Food_Scanner.users.models import Profile, History


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
        contents - value of fragment in URL
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
        type - obj (HttpRequest)
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
    history = History.objects.create(name=itemName, userId=profile)    


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
