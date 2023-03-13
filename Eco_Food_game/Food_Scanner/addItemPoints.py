import sqlite3
from users.models import Profile


def isAdd(fragment) -> bool:
    """
    Checks whether the fragment is an Add request
    :param fragment: value of fragment in URL
        type - string
    :return True when the fragment is an Add request otherwise false
        type - boolean
    """

    if fragment.startswith("Add"):
        return True


def showPts(fragment) -> dict:
    """
    Generates an attributes for when a user clicks Add X Points
    Splits fragment and returns addPts as points and isAdd as True other than them 2 it returns an 
    essentially empty dictionary
    :param - fragment
        type - string
        contents - value of fragment in URL
    :return - lib
        type - dictionary
        contents - all values passed to webpage, many are N/A and are unused
    """
    
    fragmentPts = fragment.split("+")
    fragmentPts2 = (fragmentPts[1]).split("+")
    points = fragmentPts2[0]

    # Could change if need to be output something else
    notAppl = "N/A"

    # Library of all values used in django templates
    lib = {
        'title': "Item page",
        'itemName' : notAppl,
        'itemEcoR' : notAppl,
        'itemEner' : notAppl,
        'itemNutr' : notAppl,
        'itemImg' : notAppl,
        'itemCO2' : notAppl,
        'itemPoints' : '',
        'isError' : False,
        'errorMsg' : "",
        'isAdd' : True,
        'addPts' : points
    }

    return lib


def addPtsDB(request, points):
    """
    Adds new points to a users score on DB
    :param1 - request
        type - HttpRequest
        content - data about request made to webpage
    :param2 - points
        type - int
        contents - points of current object to add to user's score
    :return - none
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


### Is this still necessary / are we still using rank for profile ###
### Also it doesn't work ###
### Could generate rank when a profile page is loaded instead of storing on DB - YES says Phil ###
def updateRank():
    """
    Updates rank of users according to scores in Profiles table in users.models
    :return - none
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