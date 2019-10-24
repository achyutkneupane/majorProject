from django import forms

class fieldForm(forms.Form):
   fone = forms.CharField(max_length = 10)
   ftwo = forms.CharField(max_length = 10)
   fthree = forms.CharField(max_length = 10)
   ffour = forms.CharField(max_length = 10)
   ffive = forms.CharField(max_length = 10)
   fsix = forms.CharField(max_length = 10)