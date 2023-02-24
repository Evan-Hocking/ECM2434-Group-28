from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Demo(models.Model):
    userName = models.CharField(max_length=15)
    userScore = models.CharField(max_length=99999,default=0)
    userEmail = models.CharField(max_length=32)
    userPw = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    rank = models.IntegerField(verbose_name='Rank', validators=[MinValueValidator(1)],default=9999)

    def __str__(self):
        return f'{self.userName,self.userScore,self.rank}'

    class Meta:
        verbose_name = 'Score List'
        verbose_name_plural = verbose_name


class Score(models.Model):
    client = models.CharField(verbose_name='Player Number', max_length=16, unique=True)
    score = models.IntegerField(verbose_name='Score', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name = 'Score List'
        verbose_name_plural = verbose_name


