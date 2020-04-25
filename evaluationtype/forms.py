from django import forms

from .models import EvaluationType,Poids

from criterion.models import Critere

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit , Row , Column
from dal import autocomplete

class EvaluationTypeForm(forms.ModelForm):

    criteres = forms.ModelMultipleChoiceField(queryset=Critere.objects.all() ,widget = autocomplete.ModelSelect2Multiple() )

    class Meta:
        model = EvaluationType
        fields = ('libelle_evaluationtype','criteres')
        widgets = {
            'libelle_evaluationtype':forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('libelle_evaluationtype', css_class='form-group col-md-6 mb-0'),
                Column('criteres', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Suivant')
        )


class PoidsForm(forms.Form):
    def __init__(self,*args,**kwargs):
        id = kwargs.pop("id")
        super(PoidsForm, self).__init__(*args,**kwargs)

        type_evaluation = EvaluationType.objects.get(pk=id)

        for critere in type_evaluation.criteres.all():
            self.fields[critere.libelle_critere] = forms.IntegerField(widget=forms.NumberInput (attrs={'min':0,'max':100}))
