from django import forms
from .models import *


class ReceptForm(forms.ModelForm):
    class Meta:
        model = Recept
        fields = ['name', 'types', 'description', 'img']




