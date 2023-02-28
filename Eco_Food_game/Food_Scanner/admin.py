from django.contrib import admin
from .models import Demo
from users.models import Scores

# Register your models here.

admin.site.register(Demo)
admin.site.register(Scores)