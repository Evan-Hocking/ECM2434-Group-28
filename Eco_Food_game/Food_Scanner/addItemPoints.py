import sqlite3
from users.models import Profile

"""
Checks whether the fragment is an Add request
param - fragment
    type - string
    contents - value of fragment in URL
return - TRUE
    type - boolean
    contents - true signifies the user has pressed the add points button
"""
def isAdd(fragment):
    if fragment.startswith("Add"):
        return True

"""
Generates an attributes for when a user clicks Add X Points
Splits fragment and returns addPts as points and isAdd as True other than them 2 it returns an 
essentially empty dictionary
param - fragment
    type - string
    contents - value of fragment in URL
return - lib
    type - dictionary
    contents - all values passed to webpage, many are N/A and are unused
"""
def showPts(fragment):
    fragmentPts = fragment.split("+")
    fragmentPts2 = (fragmentPts[1]).split("+")
    points = fragmentPts2[0]
    errorMsg = ""
    isError = False
    itemName = "N/A"
    itemEcoR = "N/A"
    itemEner = "N/A"
    itemNutr = "N/A"
    itemImg = "N/A"
    itemProc = "N/A"

    lib = {
      'itemName' : itemName,
      'itemEcoR' : itemEcoR,
      'itemEner' : itemEner,
      'itemNutr' : itemNutr,
      'itemProc' : itemProc,
      'itemImg' : itemImg,
      'itemPoints' : '',
      'isError' : isError,
      'errorMsg' : errorMsg,
      'isAdd' : True,
      'addPts' : points
    }

    return lib

"""
Adds new points to a users score on DB
param1 - request
    type - HttpRequest object
    content - data about request made to webpage
param2 - points
    type - int
    contents - points of current object to add to user's score
"""
def addPtsDB(request, points):
    
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
### Also it doesn't work / doesnt show up correctly on site ###
### Could generate rank when a profile page is loaded instead of storing on DB ###
"""
Updates rank of users according to scores in Profiles table in users.models
"""
def updateRank():
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