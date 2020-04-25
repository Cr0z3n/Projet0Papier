from django.db import models

from criterion.models import Critere


# Create your models here.
class EvaluationType(models.Model):
    libelle_evaluationtype= models.CharField(max_length=255)
    criteres = models.ManyToManyField(Critere, through='Poids',related_name='criteres')

    def __str__(self):
        return self.libelle_evaluationtype

class Poids(models.Model):
    type_evaluation = models.ForeignKey(EvaluationType,on_delete=models.CASCADE)
    critere = models.ForeignKey(Critere,on_delete=models.CASCADE)
    poids = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.poids)
