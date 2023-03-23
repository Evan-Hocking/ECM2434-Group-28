#-------------------------------------------------------------------------------
# Name:        models.py
# Purpose:     Creates database tables (Profiles and History)
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

"""
In the models.py, it contain the database property and shows what did we extend base on oringinal database.
We extend two part:
Profile: contain user score, rank, and profile image.
History:contain the food that user has submit.
"""

class Profile(models.Model):
    """
    Create Profile model with user, image, score and userRank fields to be added to the database
    """
    # Defining the fields and types
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    userRank = models.IntegerField(default=0)
    Drink = models.IntegerField(default=0)
    Snack = models.IntegerField(default=0)
    Vegetable = models.IntegerField(default=0)
    Protein = models.IntegerField(default=0)
    Fruit = models.IntegerField(default=0)

    
    def __str__(self):
        """
        Display the table with the title of "usernams profile"
        When it calls itself, returns the usernames
        :param self: The instance of the object (Profile)
            type - Profile
        :return: The usernames from the database
        """
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs) -> None:
        """
        When an instance of the model is saved to the database resize the image to 300,300
        :param self: The instance of Profile object
        :param args: 
        :param kwargs:
        :return: None
        """
        super().save()

        img = Image.open(self.image.path)

        '''make image fit on web'''
        if img.height > 300 or img.width > 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.image.path)


class History(models.Model):
    """
    Create History model with name, UserId adn date_Added fields to be added to the database
    """
    name = models.CharField(max_length=200)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_Added = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    # image = models.CharField(max_length=9999, blank=True)
    """
    When it calls itself, returns the usernames
    @param self - The object
    @return The usernames from the database
    """
    def __str__(self):
        """
        When it calls itself, returns the usernames
        :param self: The instance of the object (Profile)
            type - obj (Profile)
        :return: The usernames from the database
        """
        return f'{self.name}'

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         outputSize = (300, 300)
    #         img.thumbnail(outputSize)
    #         img.save(self.image.path)

class Achievements(models.Model):
    """
    Create Achievements model with all the achievements in the database
    """
    Id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    First_Scan = models.BooleanField(default=False)
    points_50 = models.BooleanField(default=False) 
    points_250 = models.BooleanField(default=False)
    points_500 = models.BooleanField(default=False)
    max_Score = models.BooleanField(default=False)
    All_cat = models.BooleanField(default=False)
    Top_10 = models.BooleanField(default=False)
    Top_5 = models.BooleanField(default=False)
    Top_3 = models.BooleanField(default=False)
    Top_1 = models.BooleanField(default=False)

    def __Str__(self):
        """
        Gets the name of the profile
        :return: The name of the user profile
        """
        return f'{self.Profile.name}'

