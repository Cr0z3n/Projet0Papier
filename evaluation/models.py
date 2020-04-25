from django.db import models


# Create your models here.
class Note(models.Model):
    libelle_critere = models.CharField(max_length=50)
    valeur = models.IntegerField()

    def __str__(self):
        return '{} : {}'.format(self.libelle_critere,str(self.valeur))
