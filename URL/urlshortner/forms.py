from django import forms
from .models import url

class Rawform(forms.Form):
    url1 = forms.CharField()