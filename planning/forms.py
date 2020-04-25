from django import forms


from user.models import Profil
from evaluationtype.models import EvaluationType

from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit , Row , Column

from dal import autocomplete
import datetime


from bootstrap_datepicker_plus import DatePickerInput , TimePickerInput



from django.forms import DateInput
from .models import Event

class EventForm(forms.ModelForm):

    evaluateurs = forms.ModelMultipleChoiceField(queryset=User.objects.filter(profil__fonctions__name='Evaluateurs'), to_field_name='username' ,widget = autocomplete.ModelSelect2Multiple() )
    eleves = forms.ModelMultipleChoiceField(queryset=User.objects.filter(profil__fonctions__name='Eleves'), widget = autocomplete.ModelSelect2Multiple() )
    responsable_parcours = forms.ModelMultipleChoiceField(queryset=User.objects.filter(profil__fonctions__name='Responsables de parcours'), widget = autocomplete.ModelSelect2Multiple() )
    type_evaluation =forms.ModelMultipleChoiceField (queryset = EvaluationType.objects.all(), widget = autocomplete.ModelSelect2Multiple() )

    class Meta:
        model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
      'start_time': DatePickerInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DatePickerInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'libelle_evaluation':forms.TextInput()
      }
        fields = ('start_time','end_time','libelle_evaluation','evaluateurs','eleves','responsable_parcours','type_evaluation')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.helper.layout = Layout(
            Row(
                Column('libelle_evaluation', css_class='form-group col-md-6 mb-0'),
                Column('eleves', css_class='form-group col-md-6 mb-0'),
                Column('evaluateurs', css_class='form-group col-md-6 mb-0'),
                Column('responsable_parcours', css_class='form-group col-md-6 mb-0'),
                Column('type_evaluation', css_class='form-group col-md-6 mb-0'),
                Column('start_time', css_class='form-group col-md-6 mb-0'),
                Column('end_time', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),

            Submit('submit', 'Enregistrer')
        )
