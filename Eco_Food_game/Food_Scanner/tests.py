# -------------------------------------------------------------------------------
# Name:        tests.py
# Purpose:     Tests the django functions in the project
#
# Author:      Hao Lun Lin
# -------------------------------------------------------------------------------
from django.test import TestCase
from .addItemPoints import isAdd, showPts, addPtsHistDB, updateRank
from .models import Demo


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

        print("isAdd() METHOD TEST PASSED")


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

        print("showPts() METHOD TEST PASSED")


class DemoModelTest(TestCase):
    """
    The class for testing the Demo Class from addItemPoints module
    """

    def setUp(self):
        """
        Sets up the demo object for testing use
        """
        Demo.objects.create(
            userName='test_user',
            userEmail='test_email@example.com',
            userPw='test_password',
            role='test_role',
            userScore=100,
        )


    def test_demo_model(self):
        """
        Getting the demo object from the database
        """
        # Gets the demo object from the database
        demo = Demo.objects.get(userName='test_user')
        self.assertEqual(demo.userEmail, 'test_email@example.com')
        self.assertEqual(demo.userPw, 'test_password')
        self.assertEqual(demo.role, 'test_role')
        self.assertEqual(demo.userScore, 100)

        # Delete the demo object that is used for testing
        demo.delete()

        print("Demo CLASS TEST PASSED")


# class TestViews(TestCase):
#     """
#     The class for testing the module views
#     """

#     def testHome(self):
#         """
#         Testing the home method from views.py
#         """
#         home()

#     def testAbout(self):
#         """
#         Testing the about method from views.py
#         """

#     def testLeaderboard(self):
#         """
#         Testing the leaderboard method from views.py
#         """

#     def testItem(self):
#         """
#         Testing the about method from views.py
#         """
