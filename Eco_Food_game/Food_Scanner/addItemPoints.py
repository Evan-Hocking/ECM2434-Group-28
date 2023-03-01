import sqlite3

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

""" def addPtsDB(points):
    # Connect to the database (create a new file if it doesn't exist)
    conn = sqlite3.connect('example.db')

    # Create a table

    # Insert a record
    conn.execute('INSERT INTO users_profile (name, email) VALUES (?, ?)', ('John', 'john@example.com'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close() """