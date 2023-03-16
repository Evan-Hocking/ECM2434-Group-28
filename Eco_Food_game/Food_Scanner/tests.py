#-------------------------------------------------------------------------------
# Name:        tests.py
# Purpose:     Tests
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.test import TestCase
from openFoodFactsPull import getProduct
import logging
logging.basicConfig(level=logging.DEBUG)
# Create your tests here.




#tests Null input into getProduct() Function
try:
    logging.debug(getProduct())
except:
    logging.error("Null input Error")

#tests a text input into getProduct()
try:
    logging.debug(getProduct('hello'))
except:
    logging.error("text input error")

#tests an int number into getProduct()
try:
    logging.debug(getProduct(80135463))
except:
    logging.error("int input error")

#tests a string number input to getProduct()
try:
    logging.debug(getProduct("80135463"))
except:
    logging.error("string input error")

#tests a number that is not a valid barcode
try:
    logging.debug(getProduct(123))
except:
    logging.error("non present barcode")

#tests if a dictionary is returned
if type(getProduct(80135463)) is dict:
    logging.debug("Correct return type")
else:
    logging.debug(type(getProduct(80135463)))
    logging.error("return type error")

#tests when ecoscore is not present
try:
    lib = getProduct(3017620422003)
    logging.debug(lib['ecoRating'])
except:
    logging.error('Ecoscore Error')

#tests when non english image is present
try:
    lib = getProduct(3228857001316)
    logging.debug(lib['image'])
except:
    logging.error('Foreign Img Error')

#tests when no image is present
try:
    lib = getProduct(7622210713780)
    logging.debug(lib['image'])
except:
    logging.error('No Img Error')

#tests when no nutriscore is present
try:
    lib = getProduct(3033710084913)
    logging.debug(lib['nutriscore'])
except:
    logging.error('No Nutriscore Error')