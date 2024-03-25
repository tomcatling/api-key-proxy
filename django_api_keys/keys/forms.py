from django import forms
from django.forms import ModelForm
 
from .models import *
 
 
class InternalKeyForm(forms.ModelForm):
 
    class Meta:
        model = InternalKey
        fields = ['name']