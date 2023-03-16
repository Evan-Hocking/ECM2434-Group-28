#-------------------------------------------------------------------------------
# Name:        signals.py
# Purpose:     Creates and saves user profiles
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) # This function is a signal receiver for the User model's post_save signal
def create_profile(sender, instance, created, **kwargs) -> None:
    """
    A signal receiver function that creates a new Profile object whenever a User object is created
    :param sender: The class of the model sending the signal
        type - class
    :param instance: The actual instance of the model that sent the signal
        type - obj
    :param created: A flag indicating if the instance was created or updated
        type - bool
    :param **kwargs: Additional keyword arguments passed to the signal
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) # This function is a signal receiver for the User model's post_save signal
def save_profile(sender, instance, **kwargs) -> None:
    """
    A signal receiver function that saves a Profile object whenever a User object is saved
    :param sender: The class of the model sending the signal
        type - class
    :param instance: The actual instance of the model that sent the signal
        type - obj
    :param **kwargs: Additional keyword arguments passed to the signal
    """
    instance.profile.save()
