from django import forms

from .models import *


class ProfilForm(forms.ModelForm):
    fonctions = forms.ModelMultipleChoiceField(queryset=Fonction.objects, widget=forms.CheckboxSelectMultiple(), required=False)
