#------------------------------------------------------------------------------------------------------
# Name: itemRequest.py
# Purpose: Uses barcode entered by user to find all an a specifc items attributes using getProduct()
#
# Author: Ryan Gascoigne-Jones
#------------------------------------------------------------------------------------------------------
from .openFoodFactsPull import getProduct


def itemAttributesDict(barcode) -> dict:
    """
    Finds and generates all attributes for a specified item for use on the item page
    :param barcode: value of barcode passed in url
        type - string
    :return lib: all attributes of an item
        type - dictionary
    """

    # Uses func from openFoodFactsPull.py
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

    # Library of all values used in django templates
    lib = {
      'title' : "Item page",
      'itemName' : itemName,
      'itemEcoR' : itemEcoR,
      'itemEner' : itemEner,
      'itemNutr' : itemNutr,
      'itemImg' : itemImg,
      'itemCO2' : itemCO2,
      'itemPoints' : itemPoints,
      'isError' : isError,
      'errorMsg' : errorMsg,
      'isAdd' : False
    }

    return lib

  
# Decided not to use
"""itemProc = itemDict['processed']
if itemProc.startswith("en"):
    itemProcStr = (itemDict['processed']).split(":")
    itemProcStr2 = (itemProcStr[1]).split("-")
    itemProc = itemProcStr2[0]"""