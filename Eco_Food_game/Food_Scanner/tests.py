# -------------------------------------------------------------------------------
# Name:        tests.py
# Purpose:     Tests the django functions in the project
#
# Author:      Hao Lun Lin
# -------------------------------------------------------------------------------
from django.test import TestCase
from .addItemPoints import isAdd, showPts, addPtsHistDB, updateRank
# from .models import Profile, History


class AddItemPointsTestCase(TestCase):
    """
    The class for testing the module addItemPoints
    """

    def testIsAdd(self):
        """
        Testing the isAdd method from addItemPoints.py
        """
        # tests a null input into isAdd() Function
        self.assertIsNone(isAdd(), "IA Err: Null input Error")

        # tests a text input into isAdd()
        self.assertFalse(isAdd("hello"), "IA Err: text input error")

        # tests an int number into getProduct(), validity irrelevant
        self.assertTrue(isAdd(80135463), "IA Err: int input error")

        # tests a string number input to isAdd(), validity irrelevant
        self.assertTrue(isAdd("80135463"), "IA Err: string input error")

        # tests if a boolean is returned
        self.assertIsInstance(isAdd("testing"), bool,
                              "IA Err: return type error")

        # tests if a valid input to isAdd()
        self.assertTrue(isAdd("AddTestCase"), "IA Err: Valid input error")

        # tests if an invalid input to isAdd()
        self.assertFalse(isAdd("falseCase"), "IA Err: Invalid input error")

    def testShowPts(self):
        """
        Testing the showPts method from addItemPoints.py
        """
        # tests a null input into showPts() Function
        self.assertIsNone(showPts(), "SP Err: Null input Error")

        # tests a text input into showPts()
        self.assertFalse(showPts("hello"), "SP Err: text input error")

        # tests an int number into showPts(), validity irrelevant
        self.assertTrue(showPts(80135463), "SP Err: int input error")

        # tests a string number input to showPts(), validity irrelevant
        self.assertTrue(showPts("80135463"), "SP Err: string input error")

        # tests if a dictionary is returned
        self.assertIsInstance(showPts(
            "Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29"), dict, "SP Err: return type error")

        # tests if the title is present in the returned dictionary
        self.assertIn('title', showPts(
            "Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29"), "SP Err: no title error")

        # tests if the itemName is present in the returned dictionary
        self.assertIn('itemName', showPts(
            "Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29"), "SP Err: no itemName error")

        # tests if the addPts is present in the returned dictionary
        self.assertIn('addPts', showPts(
            "Add+1+pts+for+Buxton+Still+Mineral+Water+Sportscap+%2812+x+75+cl%29"), "SP Err: no addPts error")


# class TestModels(TestCase):
#     """
#     The class for testing the module models
#     """

#     def setUp(self):
#         """
#         Sets up the objects
#         """
