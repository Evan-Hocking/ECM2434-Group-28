# -------------------------------------------------------------------------------
# Name:        testCustom.py
# Purpose:     Tests ran by github actions
#
# Author:      Evan Hocking, Hao Lun Lin
# -------------------------------------------------------------------------------
from .addItemPoints import isAdd, showPts
from .itemRequest import itemAttributesDict
from .openFoodFactsPull import getProduct, getPoints
import onCampus

# -------------------------------------------------------------------------------
# Name:        addItemPoints.py
# -------------------------------------------------------------------------------


def testIsAdd():
    """
    Testing the isAdd method from addItemPoints.py
    """
    # tests a null input into isAdd() Function
    assert isAdd(), "IA Err: Null input Error"

    # tests a text input into isAdd()
    assert isAdd("hello"), "IA Err: text input error"

    # tests an int number into getProduct(), validity irrelevant
    assert isAdd(80135463), "IA Err: int input error"

    # tests a string number input to isAdd(), validity irrelevant
    assert isAdd("80135463"), "IA Err: string input error"

    # tests if a boolean is returned
    assert type(isAdd("testing")) is bool, "IA Err: return type error"

    # tests if a valid input to isAdd()
    assert isAdd("AddTestCase") == True, "IA Err: Valid input error"

    # tests if an invalid input to isAdd()
    assert isAdd("falseCase") == False, "IA Err: Invalid input error"

    print("isAdd() METHOD TEST PASSED")


def testShowPts():
    """
    Testing the showPts method from addItemPoints.py
    """
    # tests a null input into isAdd() Function
    assert showPts(), "SP Err: Null input Error"

    # tests a text input into isAdd()
    assert showPts("hello"), "SP Err: text input error"

    # tests an int number into getProduct(), validity irrelevant
    assert showPts(80135463), "SP Err: int input error"

    # tests a string number input to isAdd(), validity irrelevant
    assert showPts("80135463"), "SP Err: string input error"

    # tests if a dictionary is returned
    assert type(showPts("Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29")
                ) is dict, "SP Err: return type error"

    # tests if the title is present in the returned dictionary
    assert showPts("Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29")[
        'title'], "SP Err: no title error"

    # tests if the itemName is present in the returned dictionary
    assert showPts("Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29")[
        'itemName'], "SP Err: no title error"

    # tests if the addPts is present in the returned dictionary
    assert showPts("Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29")[
        'addPts'], "SP Err: no addPts error"

    print("showPts() METHOD TEST PASSED")

# -------------------------------------------------------------------------------
# Name:        itemRequest.py
# -------------------------------------------------------------------------------


def testItemAttributesDict():
    """
    Testing the itemAttributesDict function from the itemRequest.py
    """
    # tests Null input into itemAttributesDict() Function
    assert itemAttributesDict(), "IAD Erro: OFFP Err - null input error"

    # tests a text input into itemAttributesDict()
    assert itemAttributesDict("hello"), "IAD Erro: OFFP Err - text input error"

    # tests an int number into itemAttributesDict(), validity irrelevant
    assert itemAttributesDict(
        80135463), "IAD Erro: OFFP Err - integer input error"

    # tests a string number input to itemAttributesDict(), validity irrelevant
    assert itemAttributesDict(
        "80135463"), "IAD Erro: OFFP Err - string input error"

    # tests if a dictionary is returned from itemAttributesDict() Function
    assert type(itemAttributesDict(80135463)
                ) is dict, "IAD Err: return type error"

    # tests when title is not present
    assert getProduct(3017620422003)[
        'title'], 'IAD Err: No title (Item page) error'

    # tests when itemName is not present
    assert getProduct(7622210713780)['itemName'], 'IAD Err: no item name error'

    # tests when itemEcoR is not present
    assert getProduct(3033710084913)[
        'itemEcoR'], 'IAD Err: no item eco rating error'

    # tests when itemEner is not present
    assert getProduct(3033710084913)[
        'itemEner'], 'IAD Err: no item energy error'

    # tests when itemNutr, is not present
    assert getProduct(3033710084913)[
        'itemNutr'], 'IAD Err: no item nutrition error'

    # tests when itemImg is not present
    assert getProduct(3033710084913)['itemImg'], 'IAD Err: no item image error'

    # tests when itemCO2 is not present
    assert getProduct(3033710084913)['itemCO2'], 'IAD Err: no item CO2 error'

    # tests when itemPoints is not present
    assert getProduct(3033710084913)[
        'itemPoints'], 'IAD Err: no item points error'

    # tests when isError is not present
    assert getProduct(3033710084913)['isError'], 'IAD Err: no isError error'

    # tests if isError is an integer data type
    assert type(getProduct(3017620422003)[
                'isError']) is bool, 'IAD Err: isError type error'

    # # tests when errorMsg is not present
    # assert getProduct(3033710084913)['errorMsg'], 'IAD Err: No isError error'

    # tests when isAdd is not present
    assert getProduct(3033710084913)['isAdd'], 'IAD Err: no isAdd error'

    # tests if isAdd is an integer data type
    assert type(getProduct(3017620422003)[
                'isAdd']) is bool, 'IAD Err: isAdd type error'

    print("itemAttributesDict() METHOD TEST PASSED")


# -------------------------------------------------------------------------------
# Name:        openFoodFactsPull.py
# -------------------------------------------------------------------------------

def testOpenFoodFacts():
    """
    Test suite for openFoodFactsPull.py
    """
    # tests Null input into getProduct() Function
    assert getProduct(), "OFFP Err: Null input Error"

    # tests a text input into getProduct()
    assert getProduct("hello"), "OFFP Err: text input error"

    # tests an int number into getProduct(), validity irrelevant
    assert getProduct(80135463), "OFFP Err: int input error"

    # tests a string number input to getProduct(), validity irrelevant
    assert getProduct("80135463"), "OFFP Err: string input error"

    # tests a number that is not a valid barcode
    assert getProduct(123), "OFFP Err: non present barcode"

    # tests if a dictionary is returned
    assert type(getProduct(80135463)) is dict, "OFFP Err: return type error"

    # tests when ecoscore is not present
    assert getProduct(3017620422003)['ecoRating'], 'OFFP Err: Ecoscore Error'

    # tests when non english image is present
    assert getProduct(3228857001316)['image'], 'OFFP Err: Foreign Img Error'

    # tests when no image is present
    assert getProduct(7622210713780)['image'], 'OFFP Err: No Img Error'

    # tests when no nutriscore is present
    assert getProduct(3033710084913)[
        'nutriscore'] == "n/a", 'OFFP Err: No Nutriscore'

    # tests when no CO2 data is available
    assert getProduct(3017620422003)['co2'], 'OFFP Err: co2 Error'

    # tests if points are type int
    assert type(getProduct(3017620422003)[
                'points']) is str, 'OFFP Err: points type Error'

    # tests if too high co2 used for score returns positive int
    assert type(getPoints("10000", "E")) is str and int(
        getPoints("10000", "E")) >= 1, "OFFP Err: negative points 1"

    # tests if n/a used for points generation
    assert type(getPoints("100", "n/a")) is str and int(getPoints("100",
                                                                  "E")) >= 1, "OFFP Err: negative points 2"

    print("OFFP TEST PASS")

# -------------------------------------------------------------------------------
# Name:        onCampus.py
# -------------------------------------------------------------------------------


def testOnCampus():
    """
    test suite for onCampus.py
    """
    # tests if geolocation pull was successful
    assert not (onCampus.getLocation() ==
                "Err: Geolocation Failed"), "OC Err: Geolocation Failed"

    # tests if latitude is present
    assert not (onCampus.getLocation() ==
                "Err: latitude not found"), "OC Err: Latitude not found"

    # tests if longitude is present
    assert not (onCampus.getLocation() ==
                "Err Longitude not found"), "OC Err: Longitude not found"

    # tests return is bool
    assert type(onCampus.isOnCampus()) is bool, "OC Err wrong type return"

    print("OC TEST PASS")

# -------------------------------------------------------------------------------
# END OF TESTS
# -------------------------------------------------------------------------------


def main():
    """
    Runs all the test methods within this module
    """
    # addItemPoints - isAdd(), showPts()
    # Other test functions are in tests.py
    testIsAdd()
    testShowPts()

    # itemRequest
    testItemAttributesDict()

    # openFoodFactsPull
    testOpenFoodFacts()

    # onCampus
    testOnCampus()


# Run all the test methods
main()
