#-------------------------------------------------------------------------------
# Name:        models.py
# Purpose:     Creates database Demo table with defined fields (i.e. Score and Rank)
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from PIL import Image


class Demo(models.Model):
    """
    Create the Demo table in the data base with the defined fields of the specified type
    """
    userName = models.CharField(max_length=15)
    userEmail = models.CharField(max_length=32)
    userPw = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    userScore = models.IntegerField(verbose_name='Score', default=0)

    
    def __str__(self) -> str:
        """
        Display the table with the title of "username , score, rank"
        :return: The string representation of the object (user's username, score and rank)
            type - str
        """
        return f'{self.userName, self.userScore, self.rank}'

    
    class Meta:
        verbose_name = 'Player List'
        verbose_name_plural = verbose_name

        
class Rank(models.Model):
    """
    Create the Demo table in the data base with the defined fields of the specified type
    """
    c_id = models.OneToOneField(
        Demo, on_delete=models.CASCADE, primary_key=True,)
    rank = models.IntegerField(verbose_name='rank', validators=[
                               MinValueValidator(1)])


class Score(models.Model):
    """
    Create the Demo table in the data base with the defined fields of the specified type
    """
    player = models.ForeignKey(Demo, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name='Score', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    rank = models.IntegerField(verbose_name='Rank', validators=[
                               MinValueValidator(1)], default=9999)

    
    def __str__(self) -> str:
        """
        Display the table with the title of "username , score, rank"
        :param self: The instance of the Score object
            type - obj (Score)
        :return: The string representation of the object (self and rank)
            type - str
        """
        return f'{self.score, self.rank}'

    
    class Meta:
        verbose_name = 'Score List'
        verbose_name_plural = verbose_name

########################### Tried this ##################################
class Image(models.Model):
    name = models.CharField(max_length=200,default="image")
    image = models.ImageField(upload_to='barcode_imgs')

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        """
        Save the image to the server
        :param self:
        :param args:
        :param kwargs:
        """
        super().save()

        #img = Image.open(self.image.path)
