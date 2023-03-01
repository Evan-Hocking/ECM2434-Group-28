from .openFoodFactsPull import getProduct
# from .views import barcode

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
    itemScore = 25
  elif itemEcoR == "B":
    itemScore = 15
  elif itemEcoR == "C":
    itemScore = 8
  elif itemEcoR == "D":
    itemScore = 4
  else:
    itemScore = 1

  lib = {
     'itemName' : itemName,
     'itemEcoR' : itemEcoR,
     'itemEner' : itemEner,
     'itemNutr' : itemNutr,
     'itemProc' : itemProc,
     'itemImg' : itemImg,
     'itemScore' : itemScore,
     'isError' : isError,
     'errorMsg' : errorMsg,
  }

  return lib

  
