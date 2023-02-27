from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Scores(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    userScore = models.CharField(max_length=99999)

    def __str__(self):
        return self.userName
