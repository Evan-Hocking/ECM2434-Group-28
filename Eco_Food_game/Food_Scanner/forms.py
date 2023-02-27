from django import forms

class BarcodeEntry(forms.Form):
    barcodeNumber = forms.CharField()
