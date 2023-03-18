import json

with open('Eco_Food_game/config.json') as json_config:
    config = json.load(json_config)

def zeroScore(adminCode, userID):
    if not(adminCode == config["adminCode"]):
        print("PERMISSION DENIED: INVALID ADMIN CODE")
        return
    #zero score code

