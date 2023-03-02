import json
import openfoodfacts

def is_number(value):
    """Tests if Variable is a number"""
    try:
        int(value)
        return True
    except ValueError:
        return False
    
    
def getImage(foodDict):
    """Gets an image from the given dictionary
    If no image is present the system will attempt to find another
    If still unsuccessful a default is returned"""
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
        
       
def getProduct(barcode=0):
    """Takes a barcode argument as either string or int
    - Tests barcode validity
    - Requests data from OpenFoodFacts Database
    - Extracts required data to dictionary
    - Return Dictionary
    """
    #tests if number
    if not is_number(barcode):
        return("Err: Invalid Barcode")
    #api request
    try:
        request     =   openfoodfacts.products.get_product(str(barcode))
        product = request['product']
    except:
        return ("Err: Request Error")
    
    #tests if api request was success
    if request['status']==0:
        return ("Err: Product not found")
    
    #gets name from dictionary
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
            name    = "n/a"
            
    #pulls other data from dictionary
    try:
        cal         =   product['nutriments']['energy-kcal_100g']
    except:
        cal         =   "n/a"
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
    
    #condenses pulled data to dictionary lib
    lib         =   {
        'barcode':str(barcode),
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'processed':processed,
        'image':img}
    
    #makes missing data appear in a consistent format
    for x in range(0,len(lib)):
        if str(list(lib.values())[x]) == "" or str(list(lib.values())[x]) == "unknown" or str(list(lib.values())[x]) == "['unknown']":
            lib[list(lib.keys())[x]] = "n/a"

    return lib
