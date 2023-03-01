from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            outputSize = (300, 300)
            img.thumbnail(outputSize)
            img.save(self.image.path)


# class History(models.Model):
#     name = models.CharField(max_length=200)
#     userId = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     image = models.CharField(max_length=9999)

#     def __str__(self):
#         return f'{self.user.profile.name}'

#     def save(self, *args, **kwargs):
#         super().save()

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             outputSize = (300, 300)
#             img.thumbnail(outputSize)
#             img.save(self.image.path)
