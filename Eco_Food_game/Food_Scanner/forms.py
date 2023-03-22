#-------------------------------------------------------------------------------
# Name:        forms.py
# Purpose:     create forms for the user to added information to databases
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------

from django import forms
from .models import *

class addImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']