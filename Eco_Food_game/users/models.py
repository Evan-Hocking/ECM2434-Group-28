#-------------------------------------------------------------------------------
# Name:        models.py
# Purpose:     Creates database tables 
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

"""
In the models.py, it contain the database property and shows what did we extend base on oringinal database.
We extend two part:
Profile: contain user score, rank, and profile image.
History:contain the food that user has submit.
"""

class Profile(models.Model):
<<<<<<< HEAD
    """
    Create Profile model with user, image, score and userRank fields to be added to the database
    """

    #Define the fields and types
=======
    
    '''Property set up: connect with original database, add score, rank and profile image in old database'''
>>>>>>> f77f22e041cb022992ea6655049bf780c28c07d5
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    userRank = models.IntegerField(default=0)
    Drink = models.IntegerField(default=0)
    Snack = models.IntegerField(default=0)
    Vegetable = models.IntegerField(default=0)
    Protein = models.IntegerField(default=0)
    Fruit = models.IntegerField(default=0)

    #Display the table with the title of "usernams profile"
    def __str__(self):
        """
        When it calls itself, returns the usernames
        @param self - The object
        @return The usernames from the database
        """
        return f'{self.user.username} Profile'
<<<<<<< HEAD

    #When an instance of the model is saved to the database resize the image to 300,300
=======
    
        """
        save the image and make it fit in Profile web
        @param image - jpg file etc.
        """
>>>>>>> f77f22e041cb022992ea6655049bf780c28c07d5
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        '''make image fit on web '''
        if img.height > 300 or img.width > 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.image.path)


class History(models.Model):
<<<<<<< HEAD
    """
    Create History model with name, UserId adn date_Added fields to be added to the database
    """

    
=======
    '''Property set up: conncet with Profile database, add date'''
>>>>>>> f77f22e041cb022992ea6655049bf780c28c07d5
    name = models.CharField(max_length=200)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_Added = models.DateTimeField(auto_now_add=True)
    # image = models.CharField(max_length=9999, blank=True)
      """
    When it calls itself, returns the usernames
    @param self - The object
    @return The usernames from the database
    """
    def __str__(self):
        return f'{self.name}'

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         outputSize = (300, 300)
    #         img.thumbnail(outputSize)
    #         img.save(self.image.path)
