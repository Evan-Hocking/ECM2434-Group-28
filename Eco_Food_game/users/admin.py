#-------------------------------------------------------------------------------
# Name:        admin.py
# Purpose:     Register extends to the databases
#
# Author:      Tom Sturgeon, Phil
#-------------------------------------------------------------------------------
from django.contrib import admin
from .models import Profile, History, Achievements


# Register extend database
admin.site.register(Profile)
admin.site.register(History)
admin.site.register(Achievements)

