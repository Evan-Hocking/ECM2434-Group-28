#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      evzy
#
# Created:     23/02/2023
# Copyright:   (c) evzy 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import logging
import openFoodFactsPull

logging.basicConfig(level=logging.DEBUG)

#tests Null input into getProduct() Function
try:
    logging.debug(openFoodFactsPull.getProduct())

except:
    logging.error("Null input Error")

#tests a text input into getProduct()
try:
    logging.debug(openFoodFactsPull.getProduct('hello'))
except:
    logging.error("text input error")

#tests an int number into getProduct()
try:
    logging.debug(openFoodFactsPull.getProduct(80135463))
except:
    logging.error("int input error")

#tests a string number input to getProduct()
try:
    logging.debug(openFoodFactsPull.getProduct("80135463"))
except:
    logging.error("string input error")

#tests a number that is not a valid barcode
try:
    logging.debug(openFoodFactsPull.getProduct(123))
except:
    logging.error("non present barcode")

#tests if a dictionary is returned
if type(openFoodFactsPull.getProduct(80135463)) is dict:
    logging.debug("Correct return type")
else:
    logging.debug(type(openFoodFactsPull.getProduct(80135463)))
    logging.error("return type error")

#tests when ecoscore is not present
try:
    lib = openFoodFactsPull.getProduct(3017620422003)
    logging.debug(lib['ecoRating'])
except:
    logging.error('Ecoscore Error')

#tests when non english image is present
try:
    lib = openFoodFactsPull.getProduct(3228857001316)
    logging.debug(lib['image'])
except:
    logging.error('Foreign Img Error')

#tests when no image is present
try:
    lib = openFoodFactsPull.getProduct(7622210713780)
    logging.debug(lib['image'])
except:
    logging.error('No Img Error')

#tests when no nutriscore is present
try:
    lib = openFoodFactsPull.getProduct(3033710084913)
    logging.debug(lib['nutriscore'])
except:
    logging.error('No Nutriscore Error')

#tests when no processed score is present
try:
    lib = openFoodFactsPull.getProduct(3760091727732)
    logging.debug(lib['processed'])
except:
    logging.error('No Processed Error')
'''
REMAINING TESTS
 - no processed score
 '''