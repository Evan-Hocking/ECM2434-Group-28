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


class Profile(models.Model):
    """
    Create Profile model with user, image, score and userRank fields to be added to the database
    """

    #Define the fields and types
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    userRank = models.IntegerField(default=0)

    #Display the table with the title of "usernams profile"
    def __str__(self):
        return f'{self.user.username} Profile'

    #When an instance of the model is saved to the database resize the image to 300,300
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

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
    # image = models.CharField(max_length=9999, blank=True)

    def __str__(self):
        return f'{self.name}'

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         outputSize = (300, 300)
    #         img.thumbnail(outputSize)
    #         img.save(self.image.path)
