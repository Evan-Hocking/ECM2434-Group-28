import json
import openfoodfacts

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def getImage(foodDict):
    try:
        img     =   foodDict['product']['selected_images']['front']['display']['en']
        return img
    except (KeyError,TypeError):
        try:
            images = foodDict['product']['selected_images']['front']['display']
            img = images[0]
            return img
        except:
            return ""
def getProduct(barcode=0):
    if not is_number(barcode):
        return("Err: Invalid Barcode")

    try:
        product     =   openfoodfacts.products.get_product(str(barcode))
    except:
        return ("Err: Request Error")
    if product['status']==0:
        return ("Err: Request Error")
    name        =   product['product']['product_name']
    cal         =   product['product']['nutriments']['energy-kcal_100g']
    nutriScore  =   product['product']['nutriscore_grade']
    ecoRating   =   product['product']['ecoscore_grade']
    processed   =   product['product']['nova_groups_tags']
    img = getImage(product)
    lib         =   {
        'barcode':barcode,
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'processed':processed,
        'image':img,
        'error':[]}

    for x in range(0,len(lib)):
        if list(lib.values())[x] == "" or list(lib.values())[x] == "unknown":
            lib["error"].append(list(lib)[x] + " not found")
    return lib
