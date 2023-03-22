#------------------------------------------------------------------------------------------------------
# Name: zero.py
# Purpose: Zeroes the score of the user
#
# Author: 
#------------------------------------------------------------------------------------------------------
import json
import sqlite3

# Configures the variables
with open('Eco_Food_game/config.json') as json_config:
    config = json.load(json_config)

def zeroScore() -> None:
    """
    Turns the score of the user to 0
    :return: None
    """
    # Asking user for pin to access admin settings
    adminCode = int(input("Enter Pin to access Admin Settings: "))
    
    # Checks if the pin entered is wrong
    if not(adminCode == config["adminCode"]):
        # Denies access for the user
        print("PERMISSION DENIED: INVALID ADMIN CODE")
        return
    
    userID = int(input("Enter Id of user to zero: "))
    try:
        # Connecting to the database
        sqliteConnection = sqlite3.connect('Eco_Food_game/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        # Updates the user score, setting it to 0
        sql_update_query = f"Update 'users_profile' set score = 0 where id = {userID}"
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        # Failed to connect to database
        print("Failed to update sqlite table", error)
    finally:
        # Closes the database connection
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# Calls the method zeroScore to set the user score to 0             
zeroScore()
