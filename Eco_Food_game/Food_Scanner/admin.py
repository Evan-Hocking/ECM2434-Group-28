#-------------------------------------------------------------------------------
# Name:        addItemPoints.py
# Purpose:     Methods to perform actions with the user's points and rank
#
# Author:      Thomas Sturgeon
#-------------------------------------------------------------------------------
from django.contrib import admin
from Food_Scanner.models import Demo
from Food_Scanner.models import Score


# Register the Demo databse table to be visible on the django admin page
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass

# Register the Score databse table to be visible on the django admin page
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
