#-------------------------------------------------------------------------------
# Name:        openFoodFactsPull.py
# Purpose:     Pulls Data from the Open Food Facts database based on Barcode
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------
import json
import openfoodfacts
from statistics import mean
def getData(barcode):
    """
    Validates barcode using isNumber
    Makes request using openfoodfacts module
    Checks status to measure return success
    @param barcode
        type string or int
    @return product
        type dictionary
    """
    #tests if number
    if not isNumber(barcode):
        return("Err: Invalid Barcode")
    #api request
    try:
        request = openfoodfacts.products.get_product(str(barcode))
        product = request['product']
    except:
        return ("Err: Request Error")

    #tests if api request was success
    if request['status']==0:
        return ("Err: Product not found")
    return product


def isNumber(value) -> bool:
    """
    Tests if Variable is a number
    @param value
        type any
    @return True if the value is an integer type otherwise false
        type bool
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
    @param - foodDict
        type - dictionary
    @return - img
        type - string
        contents - url of image
    """
    try:
        #gets english image
        img     =   foodDict['selected_images']['front']['display']['en']
        return img
    except (KeyError,TypeError):
        #finds alternative language image
        try:
            images = foodDict['selected_images']['front']['display']
            img = images[0]
            return img
        except:
            #uses default image
            return "https://world.openfoodfacts.org/images/icons/dist/packaging.svg"


def getCO2(foodDict) -> str:
    """
    gets CO2 data from dictionary
    multiplies by 100 to convert to per 100g instead of per gram
    rounds to nearest int
    @param foodDict
        type dictionary
    @return co2
        type string
    """
    try:
        co2 = foodDict['ecoscore_data']['agribalyse']['co2_total']
        co2 = str(round((co2)*100))
        return co2
    except:
        return "n/a"



def getName(foodDict) -> str:
    """
    attempts to get name
    if not available will try and find another name in the database
    @param foodDict
        type dictionary
    @return name
        type string
    """
    name = ""
    try:
        name        =   foodDict['product_name']
    except:
        for key in foodDict.keys():
            if "name" in key.lower():
                name = foodDict[key]
                if type(name) is str and name:
                    break
        if not name:
            return "n/a"
    return name


def getCalroie(foodDict):
    """
    gets calorie data from dictionary
    @param foodDict
        type dictionary
    @return cal
        type string
    """
    try:
        cal         =   foodDict['nutriments']['energy-kcal_100g']
    except:
        return "n/a"
    return cal


def getEco(foodDict):
    """
    gets EcoRating from dictionary
    @param foodDict
        type dictionary
    @return ecoRating
        type string
    """
    try:
        ecoRating   =   foodDict['ecoscore_grade']
    except:
        return "n/a"
    return ecoRating


def getNutri(foodDict):
    """
    gets nutrition score from dictionary
    @param foodDict
        type dictionary
    @return nutriScore
        type string
    """
    try:
        nutriScore  =   foodDict['nutriscore_grade']
    except:
        return "n/a"
    return nutriScore


def getPoints(CO2Dat,foodDict):
    """
    gets points by applying the function 251.026-182.582x^(0.0473541) to CO2Dat
    rounds the result to nearest positive integer
    @param CO2Dat
        type string
    @return points
        type string
    """
    ecoPointDict = {"A":25,
                "B":15,
                "C":8,
                "D":4,
                "E":1,
                }
    ecoScore = getEco(foodDict)
    try:
        ecoPoints = ecoPointDict[ecoScore]
    except:
        ecoPoints = 1
    try:
        CO2points = round(251.026 - 182.582 * int(CO2Dat) ** 0.0473541)
        if CO2points>25:
            CO2points = 25
    except:
        CO2points = 1
    if CO2points < 1:
        CO2points = 1
    points = mean((ecoPoints,CO2points))
    return str(points)


def makeDictionaryConsistent(lib) ->dict:
    """
    takes the output dictionary and makes missing data a consistent format of n/a
    @param lib
        type dictionary
    @return lib
        type dictionary
    """
    for x in range(0,len(lib)):
        if str(list(lib.values())[x]) == "" or str(list(lib.values())[x]) == "unknown" or str(list(lib.values())[x]) == "['unknown']":
            lib[list(lib.keys())[x]] = "n/a"
    return lib


def getProduct(barcode=0):
    """
    calls getData to get product information
    if is a string returns
    uses get functions to pull data from dictionary
    uses getPoints()
    generates new dictionary with data
    uses makemakeDictionaryConsistent()
    @param - barcode
        type - String or int
    @return - Dictionary
    """
    product = getData(barcode)
    if isinstance(product,str):
        return product


    name = getName(product)
    cal  = getCalroie(product)
    ecoRating = getEco(product)
    nutriScore = getNutri(product)
    img = getImage(product)
    co2 = getCO2(product)
    points = getPoints(co2,product)

    #condenses pulled data to dictionary lib
    lib         =   {
        'barcode':str(barcode),
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'image':img,
        'co2':co2,
        'points':points}

    lib = makeDictionaryConsistent(lib)
    return lib
