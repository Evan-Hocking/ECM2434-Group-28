#-------------------------------------------------------------------------------
# Name:        apps.py
# Purpose:     Configuration for the Food_Scanner Django app
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.apps import AppConfig

class FoodScannerConfig(AppConfig):
    """
    AppConfig class for the Food_Scanner Django app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Food_Scanner'
