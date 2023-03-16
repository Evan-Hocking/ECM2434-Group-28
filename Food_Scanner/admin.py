#-------------------------------------------------------------------------------
# Name:        admin.py
# Purpose:     Registers the database tables to be visible on the django admin page.
#
# Author:      Thomas Sturgeon
#-------------------------------------------------------------------------------
from django.contrib import admin
from Food_Scanner.models import Demo
from Food_Scanner.models import Score


# Register the Demo database table to be visible on the django admin page
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass

# Register the Score database table to be visible on the django admin page
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
