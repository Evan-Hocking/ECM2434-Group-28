import sqlite3
from users.models import Profile

def isAdd(fragment):
    if fragment.startswith("Add"):
        return True

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
      'itemScore' : '',
      'isError' : isError,
      'errorMsg' : errorMsg,
      'isAdd' : True,
      'addPts' : points
    }

    return lib

#def addPtsDB(points):