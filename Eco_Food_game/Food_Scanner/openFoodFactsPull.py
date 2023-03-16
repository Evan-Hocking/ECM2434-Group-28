# -------------------------------------------------------------------------------
# Name:        openFoodFactsPull.py
# Purpose:     Pulls Data from the Open Food Facts database based on Barcode
#
# Author:      Evan Hocking
# -------------------------------------------------------------------------------
import json
import openfoodfacts
from statistics import mean


def getData(barcode) -> dict:
    """
    Validates the barcode using isNumber
    Makes request using openfoodfacts module
    Checks status to measure return success
    :param barcode: The barcode of the item
        type - str or int
    :return product: The data of the product
        type dict
    """
    # tests if number
    if not isNumber(barcode):
        return ("Err: Invalid Barcode")
    # api request
    try:
        request = openfoodfacts.products.get_product(str(barcode))
        product = request['product']
    except:
        return ("Err: Request Error")

    # tests if api request was success
    if request['status'] == 0:
        return ("Err: Product not found")
    return product


def isNumber(value) -> bool:
    """
    Tests if variable is an integer type
    :param value: The input that is being tested
        type - any
    :return: True if the value is an integer type otherwise false
        type - bool
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def getImage(foodDict):
    """
    Gets an image from the given dictionary
    If no image is present the system will attempt to find another
    If still unsuccessful a default is returned
    :param foodDict: The dictionary of the item details
        type - dict
    :return img: The url of the image, if no image found default will be used
        type - str
    """
    try:
        # Gets english image
        img = foodDict['selected_images']['front']['display']['en']
        return img
    except (KeyError, TypeError):
        # Finds alternative language image
        try:
            images = foodDict['selected_images']['front']['display']
            img = images[0]
            return img
        except:
            # Uses default image
            return "https://world.openfoodfacts.org/images/icons/dist/packaging.svg"


def getCO2(foodDict) -> str:
    """
    Gets CO2 data from dictionary
    multiplies by 100 to convert to per 100g instead of per gram
    rounds to nearest int
    :param foodDict: The dictionary of the item details
        type - dict
    :return co2: The CO2 data
        type - str
    """
    try:
        co2 = foodDict['ecoscore_data']['agribalyse']['co2_total']
        co2 = str(round((co2)*100))
        return co2
    except:
        return "n/a"


def getName(foodDict) -> str:
    """
    Attempts to get the name of the item
    if not available will try and find another name in the database
    :param foodDict: The details of the item
        type - dict
    :return name: The name of the item
        type - str
    """
    name = ""
    try:
        name = foodDict['product_name']
    except:
        for key in foodDict.keys():
            if "name" in key.lower():
                name = foodDict[key]
                if type(name) is str and name:
                    break
        if not name:
            return "n/a"
    return name


def getCalroie(foodDict) -> str:
    """
    Gets the calorie data from dictionary
    :param foodDict: The details of the item
        type - dict
    :return cal: The calorie data of the item
        type - str
    """
    try:
        cal = foodDict['nutriments']['energy-kcal_100g']
    except:
        return "n/a"
    return cal


def getEco(foodDict) -> str:
    """
    Gets EcoRating from dictionary
    :param foodDict: The details of the item
        type dict
    :return: The eco rating of the item
        type - str
    """
    try:
        ecoRating = foodDict['ecoscore_grade']
    except:
        return "n/a"
    return ecoRating


def getNutri(foodDict):
    """
    Gets nutrition score from dictionary
    :param foodDict: The details of the item
        type - dict
    :return: The nutrition score of the item
        type - string
    """
    try:
        nutriScore = foodDict['nutriscore_grade']
    except:
        return "n/a"
    return nutriScore


def getPoints(CO2Dat, foodDict) -> str:
    """
    Gets points by applying the function 251.026-182.582x^(0.0473541) to CO2Dat
    rounds the result to nearest positive integer
    :param CO2Dat: The CO2 data of the item
        type - str
    :return: The calculated points of the CO2 data
        type - str
    """
    ecoPointDict = {"A": 25,
                    "B": 15,
                    "C": 8,
                    "D": 4,
                    "E": 1,
                    }
    ecoScore = getEco(foodDict)
    try:
        ecoPoints = ecoPointDict[ecoScore]
    except:
        ecoPoints = 1
    try:
        CO2points = round(251.026 - 182.582 * int(CO2Dat) ** 0.0473541)
        if CO2points > 25:
            CO2points = 25
    except:
        CO2points = 1
    if CO2points < 1:
        CO2points = 1
    points = round(mean((ecoPoints, CO2points)))
    return str(points)


def makeDictionaryConsistent(lib) -> dict:
    """
    Takes the output dictionary and makes missing data a consistent format of n/a
    :param lib: The output dictionary
        type - dict
    :return lib: The lib that has been formatted into a consitent format of n/a
        type - dict
    """
    for x in range(0, len(lib)):
        if str(list(lib.values())[x]) == "" or str(list(lib.values())[x]) == "unknown" or str(list(lib.values())[x]) == "['unknown']":
            lib[list(lib.keys())[x]] = "n/a"
    return lib


def getProduct(barcode=0) -> dict:
    """
    Calls getData to get product information
    if is a string returns
    uses get functions to pull data from dictionary
    uses getPoints()
    Generates new dictionary with data
    uses makemakeDictionaryConsistent()
    :param barcode: The barcode of the item
        type - str or int
    :return: The product information
        type - dict
    """
    product = getData(barcode)
    if isinstance(product, str):
        return product

    name = getName(product)
    cal = getCalroie(product)
    ecoRating = getEco(product)
    nutriScore = getNutri(product)
    img = getImage(product)
    co2 = getCO2(product)
    points = getPoints(co2, product)

    # Condenses pulled data to dictionary lib
    lib = {
        'barcode': str(barcode),
        'name': name,
        'energy': cal,
        'nutriscore': nutriScore,
        'ecoRating': ecoRating,
        'image': img,
        'co2': co2,
        'points': points}

    lib = makeDictionaryConsistent(lib)
    return lib
