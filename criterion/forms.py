from django import forms

from .models import Critere, Champ

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit , Row , Column
from dal import autocomplete

class CritereForm(forms.ModelForm):

    champs = forms.ModelMultipleChoiceField(queryset=Champ.objects.all() ,widget = autocomplete.ModelSelect2Multiple() )


    class Meta:
        model = Critere
        fields = ('libelle_critere','champs')
        widgets = {
            'libelle_critere':forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('libelle_critere', css_class='form-group col-md-6 mb-0'),
                Column('champs', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Enregistrer')
        )


class ChampForm(forms.ModelForm):

    class Meta:
        model = Champ
        fields = ('nom',)
        widgets = {
            'nom':forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nom', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Enregistrer')
        )


class PoidsChampForm(forms.Form):
    def __init__(self,*args,**kwargs):
        id = kwargs.pop("id")
        super(PoidsChampForm, self).__init__(*args,**kwargs)

        critere = Critere.objects.get(pk=id)
        print(critere.champs.all())
        for champ in critere.champs.all():
            self.fields[champ.nom] = forms.IntegerField(widget=forms.NumberInput (attrs={'min':0,'max':100}))
