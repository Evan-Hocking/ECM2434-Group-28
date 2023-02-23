import json
import openfoodfacts

def getProduct(barcode):
    product     =   openfoodfacts.products.get_product(str(barcode))
    name        =   product['product']['product_name']
    cal         =   product['product']['nutriments']['energy-kcal_100g']
    nutriScore  =   product['product']['nutriscore_grade']
    ecoRating   =   product['product']['ecoscore_grade']
    processed   =   product['product']['nova_groups_tags']
    try:
        img         =   product['product']['selected_images']['front']['display']['en']
    except:
        img = ""
    lib         =   {
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
