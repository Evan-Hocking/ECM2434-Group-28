# ------------------------------------------------------------------------------------------------------
# Name: itemRequest.py
# Purpose: Uses barcode entered by user to find all an a specifc items attributes using getProduct()
#
# Author: Ryan Gascoigne-Jones
# ------------------------------------------------------------------------------------------------------
from .openFoodFactsPull import getProduct, getCategory


def itemAttributesDict(barcode) -> dict:
    """
    Finds and generates all attributes for a specified item for use on the item page
    :param barcode: The value of barcode passed in url
        type - str
    :return lib: all attributes of an item
        type - dict
    """

    # Uses method from openFoodFactsPull.py to get the item information
    itemDict = getProduct(barcode)

    # Sets values for variables
    errorMsg = ""
    isError = False

    # Checks whether the barcode entered corresponds to an item in the external DB
    # If there isn't an item for the barcode then:
    if isinstance(itemDict, str):
        errorMsg = "Error: Product not found"
        isError = True
        itemName = "N/A"
        itemEcoR = "N/A"
        itemEner = "N/A"
        itemNutr = "N/A"
        itemImg = "N/A"
        itemCO2 = "N/A"
        itemPoints = 0
        tags = "N/A"

    # If there is an item for the barcode then its attributes/values
    # obtained from getProduct() are parsed and formatted.
    else:
        itemName = itemDict['name']
        itemEcoR = (itemDict['ecoRating']).upper()
        itemEner = itemDict['energy']
        itemNutr = (itemDict['nutriscore']).upper()
        itemImg = itemDict['image']
        itemCO2 = itemDict['co2']
        itemPoints = itemDict['points']
        tags = itemDict['tags']
    # Library of all values used in django templates
    lib = {
        'title': "Item page",
        'itemName': itemName,
        'itemEcoR': itemEcoR,
        'itemEner': itemEner,
        'itemNutr': itemNutr,
        'itemImg': itemImg,
        'itemCO2': itemCO2,
        'itemPoints': itemPoints,
        'isError': isError,
        'errorMsg': errorMsg,
        'tags': tags,
        'isAdd': False,
    }

    return lib
