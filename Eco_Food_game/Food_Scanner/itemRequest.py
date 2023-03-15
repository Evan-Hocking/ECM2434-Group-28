#-------------------------------------------------------------------------------
# Name:        itemRequest.py
# Purpose:     Finds and generate all attributes for a specified item for use on the item page
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from .openFoodFactsPull import getProduct


def itemAttributesDict(barcode) -> dict:
    """
    Finds and generates all attributes for a specified item for use on the item page
    :param barcode: The barcode of the specified item
        type - str
        contents - value of barcode passed in url
    :return lib: The dictionary of all attributes of an item
        type - dict
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
        itemProc = "N/A"
    
    # If there is an item for the barcode then its attributes/values
    # obtained from getProduct() are parsed and formatted.
    else:
        itemName = itemDict['name']
        itemEcoR = (itemDict['ecoRating']).upper()
        itemEner = itemDict['energy']
        itemNutr = (itemDict['nutriscore']).upper()
        itemImg = itemDict['image']
        itemProc = itemDict['processed']
        if itemProc.startswith("en"):
          itemProcStr = (itemDict['processed']).split(":")
          itemProcStr2 = (itemProcStr[1]).split("-")
          itemProc = itemProcStr2[0]

    ### Will be deprecated when Evan generates points in openFoodFactsPull.py ###
    # Generates a set number of points for each eco rating grade
    if itemEcoR == "A":
        itemPoints = 25
    elif itemEcoR == "B":
        itemPoints = 15
    elif itemEcoR == "C":
        itemPoints = 8
    elif itemEcoR == "D":
        itemPoints = 4
    else:
        itemPoints = 1

    # Library of all values used in django templates
    lib = {
      'title' : "Item page",
      'itemName' : itemName,
      'itemEcoR' : itemEcoR,
      'itemEner' : itemEner,
      'itemNutr' : itemNutr,
      'itemProc' : itemProc,
      'itemImg' : itemImg,
      'itemPoints' : itemPoints,
      'isError' : isError,
      'errorMsg' : errorMsg,
      'isAdd' : False,
      'addPts' : ''
    }

    return lib

  
