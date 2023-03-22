#-------------------------------------------------------------------------------
# Name:        openFoodFactsPull.py
# Purpose:     Pulls Data from the Open Food Facts database based on Barcode
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------
import json
import openfoodfacts
from statistics import mean


def isNumber(value) -> bool:
    """
    Tests if the value is an integer
    :param value: The input value
        type - any
    :return: True if the value is an integer type otherwise false
        type - bool
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

    
def getData(barcode) -> dict:
    """
    Gets the item data from the api using the barcode of the item
    :param barcode: The value of the item barcode
        type - str or int
    :return product: The item information of the searched barcode of the item
        type - dict
    """
    # tests if the barcode is a number
    if not isNumber(barcode):
        return("Err: Invalid Barcode")
    
    # api request that gets the product info
    try:
        request = openfoodfacts.products.get_product(str(barcode))
        product = request['product']
    except:
        return ("Err: Request Error")

    # tests if api request was success
    if request['status']==0:
        return ("Err: Product not found")
    
    return product


def getImage(foodDict):
    """
    Gets an image from the given dictionary
    If no image is present the system will attempt to find another
    If still unsuccessful a default is returned
    :param foodDict: The item information used for getting the image
        type - dict
    :return img: The url of the image that was found
        type - str
    """
    try:
        # Gets english image url
        img     =   foodDict['selected_images']['front']['display']['en']
        return img
    except (KeyError,TypeError):
        # finds alternative language image url
        try:
            images = foodDict['selected_images']['front']['display']
            img = images[0]
            return img
        except:
            # uses default image url
            return "https://world.openfoodfacts.org/images/icons/dist/packaging.svg"


def getCO2(foodDict) -> str:
    """
    Gets CO2 data from dictionary,
    multiplies by 100 to convert to per 100g instead of per gram,
    and rounds it to the nearest integer
    :param foodDict: The information of the item
        type - dict
    :return: The CO2 data of the item, returns not applicable ("n/a") if the no CO2 data is found
        type - str
    """
    try:
        co2 = foodDict['ecoscore_data']['agribalyse']['co2_total']
        co2 = str(round((co2)*100))
        return co2
    except:
        # Returns not applicable ("n/a") if the no CO2 data is found
        return "n/a"


def getName(foodDict) -> str:
    """
    Attempts to get name the item
    if not available will try and find another name in the database
    :param foodDict: The information of the item
        type - dict
    :return: The name of the item
        type - str
    """
    name = ""
    
    try:
        name = foodDict['product_name']
    except:
        # The item name cannot be found, finding another name instead
        for key in foodDict.keys():
            if "name" in key.lower():
                name = foodDict[key]
                # Checking if the name is a valid one
                if type(name) is str and name:
                    break
        # If no names are valid then return not applicable ("n/a")
        if not name:
            return "n/a"
    # Returning the name of the item
    return name


def getCalroie(foodDict) -> str:
    """
    Gets calorie data from the given item information dictionary
    :param foodDict: The information of the item
        type - dict
    :return cal: The item calories information, returns not applicable ("n/a") if the no calorie data is found
        type - str
    """
    try:
        cal = foodDict['nutriments']['energy-kcal_100g']
    except:
        # Returns not applicable ("n/a") if the no calorie information is found
        return "n/a"
    return cal


def getEco(foodDict) -> str:
    """
    Gets EcoRating from dictionary
    :param foodDict: The information of the item
        type - dict
    :return: The eco rating of the item, returns not applicable ("n/a") if the no eco rating is found
        type - str
    """
    try:
        ecoRating = foodDict['ecoscore_grade']
    except:
        # Returns not applicable ("n/a") if the no eco rating is found
        return "n/a"
    
    return ecoRating


def getNutri(foodDict) -> str:
    """
    Gets nutrition score from item's information
    :param foodDict: The information of the item
        type - dict
    :return: The nutrition score of the item
        type - str
    """
    try:
        nutriScore = foodDict['nutriscore_grade']
    except:
        # Returns not applicable ("n/a") if the no nutrition score is found
        return "n/a"
    
    return nutriScore


def getCategory(foodDict) -> list:
    """
    Gets the item tags/categories
    :param foodDict: The information of the item
        type - dict
    :return: A list of tags/categories of the item
        type - list
    """
    categories = foodDict['food_groups_tags']
    tags = []
    
    # Assigns tags (item category) to the items
    if any("beverage" in s for s in categories):
        tags.append("drink")
    elif any("fruit" in s for s in categories):
        tags.append("fruit")
    elif any("vegetables" in s for s in categories):
        tags.append("vegetables")
    elif any("snack" in s for s in categories):
        tags.append("snack")
    elif any("meat" in s for s in categories):
        tags.append("protein")
        
    return tags


def getPoints(CO2Dat,ecoScore) -> str:
    """
    Gets the points of the item by applying the function 251.026-182.582x^(0.0473541) to CO2Dat
    rounds the result to nearest positive integer
    :param CO2Dat: The CO2 data of the item
        type - str
    :param ecoScore: The eco score of the item
    :return: The points of the item
        type - str
    """
    # The item points according to the grades
    ecoPointDict = {"A":25,
                "B":15,
                "C":8,
                "D":4,
                "E":1,
                }
    
    try:
        ecoPoints = ecoPointDict[ecoScore]
    except:
        # If no eco score is found then assigns the points to 1
        ecoPoints = 1
        
    try:
        CO2points = round(251.026 - 182.582 * int(CO2Dat) ** 0.0473541)
        if CO2points > 25:
            CO2points = 25
    except:
        # If no CO2 points can be assigned then assign it to 1
        CO2points = 1
    
    # Checks if the CO2 points is calculated to be less than 1
    if CO2points < 1:
        CO2points = 1
        
    # Rounds the points to the nearest positive integer
    points = round(mean((ecoPoints,CO2points)))
    
    # Returning the points as a string
    return str(points)


def makeDictionaryConsistent(lib) -> dict:
    """
    Takes the dictionary and makes missing data a consistent format of "n/a"
    :param lib: The original dictionary that may have missing data
        type - dict
    :return: The input that has been formatted to fill in the missing data
        type - dict
    """
    for x in range(0,len(lib)):
        # Checks if there is missing data in lib
        if str(list(lib.values())[x]) == "" or str(list(lib.values())[x]) == "unknown" or str(list(lib.values())[x]) == "['unknown']":
            # Overwrites the missing data as "n/a"
            lib[list(lib.keys())[x]] = "n/a"
            
    return lib


def getProduct(barcode=0) -> dict:
    """
    Gets the item/product information with its barcode
    :param barcode: The barcode value of the item
        type - str or int
    :return: The product information that has been formatted
        type - dict
    """
    # Gets the product data
    product = getData(barcode)
    
    if isinstance(product, str):
        return product

    # Gets the details of the item
    name = getName(product)
    cal  = getCalroie(product)
    ecoRating = getEco(product)
    nutriScore = getNutri(product)
    img = getImage(product)
    co2 = getCO2(product)
    points = getPoints(co2,ecoRating)
    tags = getCategory(product)

    # Condenses pulled data to dictionary lib
    lib         =   {
        'barcode':str(barcode),
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'image':img,
        'co2':co2,
        'points':points,
        'tags':tags
        }
    
    # Fills in any missing data in lib
    lib = makeDictionaryConsistent(lib)
    return lib
