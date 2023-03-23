#-------------------------------------------------------------------------------
# Name:        forms.py
# Purpose:     create forms for the user to added information to databases
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Creating the register form
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Creating the user update form
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Creating the profile update form
    """
    
    class Meta:
        model = Profile
        fields = ['image']
