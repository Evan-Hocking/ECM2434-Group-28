#-------------------------------------------------------------------------------
# Name:        testCustom.py
# Purpose:     Tests ran by github actions
#
# Author:      Evan Hocking
#-------------------------------------------------------------------------------

from openFoodFactsPull import getProduct
import onCampus 

def testOpenFoodFacts():
    """
    test suite for openFoodFactsPull.py
    """
    #tests Null input into getProduct() Function
    assert getProduct(),"OFFP Err: Null input Error"

    #tests a text input into getProduct()
    assert getProduct("hello"),"OFFP Err: text input error"

    #tests an int number into getProduct(), validity irrelevant
    assert getProduct(80135463),"OFFP Err: int input error"

    #tests a string number input to getProduct(), validity irrelevant
    assert getProduct("80135463"),"OFFP Err: string input error"

    #tests a number that is not a valid barcode
    assert getProduct(123),"OFFP Err: non present barcode"
    
    #tests if a dictionary is returned
    assert type(getProduct(80135463)) is dict,"OFFP Err: return type error"

    #tests when ecoscore is not present
    assert getProduct(3017620422003)['ecoRating'],'OFFP Err: Ecoscore Error'

    #tests when non english image is present
    assert getProduct(3228857001316)['image'],'OFFP Err: Foreign Img Error'
    
    #tests when no image is present
    assert  getProduct(7622210713780)['image'],'OFFP Err: No Img Error'

    #tests when no nutriscore is present
    assert getProduct(3033710084913)['nutriscore']== "n/a",'OFFP Err: No Nutriscore'

    print("OFFP TEST PASS")


def testOnCampus():
    """
    test suite for onCampus.py
    """
    #tests if geolocation pull was successful
    assert not(onCampus.getLocation()== "Err: Geolocation Failed"), "OC Err: Geolocation Failed"

    #tests if latitude is present
    assert not(onCampus.getLocation() ==  "Err: latitude not found"),"OC Err: Latitude not found"

    #tests if longitude is present
    assert not(onCampus.getLocation() ==  "Err Longitude not found"),"OC Err: Longitude not found"

    #tests return is bool
    assert type(onCampus.isOnCampus()) is bool,"OC Err wrong type return"
    
    print("IO TEST PASS")
def main():
    testOpenFoodFacts()
    testOnCampus()
main()
