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
            return "https://world.openfoodfacts.org/images/icons/dist/packaging.svg"
def getProduct(barcode=0):
    if not is_number(barcode):
        return("Err: Invalid Barcode")

    try:
        request     =   openfoodfacts.products.get_product(str(barcode))
        product = request['product']
    except:
        return ("Err: Request Error")
    if request['status']==0:
        return ("Err: Product not found")
    name = ""
    try:
        name        =   product['product_name']
    except:
        for key in product.keys():
            if "name" in key.lower():
                name = product[key]
                if type(name) is str and name:
                    break

        if not name:
            name    = "name not found"
    try:
        cal         =   product['nutriments']['energy-kcal_100g']
    except:
        cal = "n/a"
    try:
        nutriScore  =   product['nutriscore_grade']
    except:
        nutriScore  = "n/a"
    try:
        ecoRating   =   product['ecoscore_grade']
    except:
        ecoRating   = "n/a"
    try:
        processed   =   product['nova_groups_tags']
        while type(processed) is list:
            processed = processed[0]
    except:
        processed   = "n/a"
    img = getImage(product)
    lib         =   {
        'barcode':str(barcode),
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'processed':processed,
        'image':img}
    for x in range(0,len(lib)):
        if str(list(lib.values())[x]) == "" or str(list(lib.values())[x]) == "unknown" or str(list(lib.values())[x]) == "['unknown']":
            lib[list(lib.keys())[x]] = "n/a"

    return lib
