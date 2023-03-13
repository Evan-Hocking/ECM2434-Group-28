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
    
    '''Property set up: connect with original database, add score, rank and profile image in old database'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    userRank = models.IntegerField(default=0)

    def __str__(self):
        """
        When it calls itself, returns the usernames
        @param self - The object
        @return The usernames from the database
        """
        return f'{self.user.username} Profile'
    
        """
        save the image and make it fit in Profile web
        @param image - jpg file etc.
        """
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        '''make image fit on web '''
        if img.height > 300 or img.width > 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.image.path)


class History(models.Model):
    '''Property set up: conncet with Profile database, add date'''
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
