from django.db import models

# Create your models here.

class Champ(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Critere(models.Model):
    libelle_critere= models.CharField(max_length=50)
    champs = models.ManyToManyField(Champ, through='PoidsChamps', related_name='champs')

    def __str__(self):
        return self.libelle_critere

class PoidsChamps(models.Model):
    champ = models.ForeignKey(Champ, on_delete=models.CASCADE)
    critere = models.ForeignKey(Critere,on_delete=models.CASCADE)
    poids_champ = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.poids_champ)
