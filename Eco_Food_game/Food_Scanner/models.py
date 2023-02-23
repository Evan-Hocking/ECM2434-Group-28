from django.db import models

# Create your models here.
class Demo(models.Model):
    userName = models.CharField(max_length=15)
    userScore = models.CharField(max_length=99999)
    userEmail = models.CharField(max_length=32)
    userPw = models.CharField(max_length = 32)
    role = models.CharField(max_length=32)