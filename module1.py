import json
import openfoodfacts
'''
product = openfoodfacts.products.get_product("80135463")
name = product['product']['product_name']
gen = product['product']['generic_name']
'''


def getProduct(barcode):
    product     =   openfoodfacts.products.get_product(str(barcode))
    name        =   product['product']['product_name']
    cal         =   product['product']['nutriments']['energy-kcal_100g']
    nutriScore  =   product['product']['nutriscore_grade']
    ecoRating   =   product['product']['ecoscore_data']['grade']
    processed   =   product['product']['nova_groups_tags']
    img         =   product['product']['selected_images']['front']['display']['en']
    lib         =   {
        'name':name,
        'energy':cal,
        'nutriscore':nutriScore,
        'ecoRating':ecoRating,
        'processed':processed,
        'image':img}
    return lib
print (getProduct(80135463))