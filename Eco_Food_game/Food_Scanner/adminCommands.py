import json
import sqlite3

with open('Eco_Food_game/config.json') as json_config:
    config = json.load(json_config)

def zeroScore(adminCode, userID):
    if not(adminCode == config["adminCode"]):
        print("PERMISSION DENIED: INVALID ADMIN CODE")
        return
    #zero score code
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = f"Update users_profile set score = 0 where id = {userID}"
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

