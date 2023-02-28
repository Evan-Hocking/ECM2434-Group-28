from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Demo(models.Model):
    userName = models.CharField(max_length=15)
    userEmail = models.CharField(max_length=32)
    userPw = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    userScore = models.IntegerField(verbose_name='Score', default=0)

    def __str__(self):
        return f'{self.userName, self.userScore, self.rank}'

    class Meta:
        verbose_name = 'Player List'
        verbose_name_plural = verbose_name


class Rank(models.Model):
    c_id = models.OneToOneField(
        Demo, on_delete=models.CASCADE, primary_key=True,)
    rank = models.IntegerField(verbose_name='rank', validators=[
                               MinValueValidator(1)])


class Score(models.Model):
    player = models.ForeignKey(Demo, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name='Score', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    rank = models.IntegerField(verbose_name='Rank', validators=[
                               MinValueValidator(1)], default=9999)

    def __str__(self):
        return f'{self.score,self.rank}'

    class Meta:
        verbose_name = 'Score List'
        verbose_name_plural = verbose_name
