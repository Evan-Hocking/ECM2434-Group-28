#-------------------------------------------------------------------------------
# Name:        apps.py
# Purpose:     AppConfig class for the Users app
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.apps import AppConfig


class UsersConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'  # Set the default primary key field type for models in this app
    name = 'users'  # Set the app name

    
    def ready(self):
        """
        Gets called when the app is ready
        """
        import users.signals  # Import the signal handlers defined in the users.signals module
