#-------------------------------------------------------------------------------
# Name:        foodHistory.py
# Purpose:     adds the food history to the webpage
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------

import sqlite3

def addToDB():
    """
    A function that takes the food scanned and adds it to the food history
    """

    #Connect to sqlite
    conn = sqlite3.connect('db.sqlite3')
    