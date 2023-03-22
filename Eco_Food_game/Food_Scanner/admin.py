#-------------------------------------------------------------------------------
# Name:        admin.py
# Purpose:     Registers the database tables to be visible on the django admin page.
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.contrib import admin
from Food_Scanner.models import Demo
from Food_Scanner.models import Score
from Food_Scanner.models import Image

# Register the Demo database table to be visible on the django admin page
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass

# Register the Score database table to be visible on the django admin page
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass

############### Is this right ##################
admin.site.register(Image)
