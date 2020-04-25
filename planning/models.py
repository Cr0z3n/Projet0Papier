from __future__ import unicode_literals
from django.db import models

from user.models import Profil

from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse
from evaluationtype.models import EvaluationType, Poids
from evaluation.models import Note
# Create your models here.
from django.db.models import Avg

from django.contrib.auth.decorators import login_required





class Event(models.Model):

    libelle_evaluation= models.CharField(max_length=255)
    evaluateurs = models.ManyToManyField(User, related_name = 'evaluateurs')
    eleves =  models.ManyToManyField(User, related_name ='eleves')
    responsable_parcours = models.ManyToManyField(User, related_name ='reponsable_parcours')

    type_evaluation=models.ManyToManyField(EvaluationType, related_name ='type_evaluation')
    notes = models.ManyToManyField(Note, blank=True,related_name='notes')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.libelle_evaluation

    @property
    def get_html_url(self):
        url = reverse('planning:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.libelle_evaluation} </a>'

    @property
    def get_html_url2(self):
        url = reverse('evaluation:event_evaluate', args=(self.id,))
        return f'<a href="{url}"> {self.libelle_evaluation} </a>'

    @property
    def note_critere(self):
        criteres_avec_notes=[]

        for type_evaluation in self.type_evaluation.all():
            for critere in type_evaluation.criteres.all():
                notes_par_critere=[]
                for note in self.notes.all():
                    if note.libelle_critere==critere.libelle_critere:
                        notes_par_critere.append(note.valeur)

                total = 0
                if len(notes_par_critere)!=0:
                    for i in notes_par_critere:
                        total+=i
                    total = total/len(notes_par_critere)
                poids = Poids.objects.get(type_evaluation = type_evaluation, critere = critere)
                criteres_avec_notes.append((critere.libelle_critere,total,poids.poids)) 
        note = 0
        poids_total = 0
        for i in criteres_avec_notes:
            note+=i[1]
            poids_total+=i[2]
        note_finale = note*20/poids_total

        return(criteres_avec_notes,note,poids_total,note_finale)
