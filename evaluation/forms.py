from django import forms

from planning.models import Event

class PostForm(forms.Form):


    def __init__(self,*args,**kwargs):
        event_id = kwargs.pop("id")
        super(PostForm, self).__init__(*args,**kwargs)

        event = Event.objects.get(pk=event_id)
        for evaluationtype in event.type_evaluation.all():
            for critere in evaluationtype.criteres.all():
                print(critere.type)
                if critere.type == 'Booleen':
                    self.fields[critere.libelle_critere] = forms.IntegerField(widget=forms.NumberInput (attrs={'min':0,'max':1}))   
                elif critere.type == 'Pourcentage':
                    self.fields[critere.libelle_critere] = forms.IntegerField(widget=forms.NumberInput (attrs={'min':0,'max':100}))
