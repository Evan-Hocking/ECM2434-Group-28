from .openFoodFactsPull import getProduct

def itemAttributesDict(barcode):

    itemDict = getProduct(barcode)

    errorMsg = ""
    isError = False
    if isinstance(itemDict, str):
        errorMsg = "Error: Product not found"
        isError = True
        itemName = "N/A"
        itemEcoR = "N/A"
        itemEner = "N/A"
        itemNutr = "N/A"
        itemImg = "N/A"
        itemProc = "N/A"
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

    lib = {
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

  
