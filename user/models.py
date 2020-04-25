from django.db import models
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db.models.signals import m2m_changed
from django.dispatch import receiver




class Fonction(models.Model):
    FONCTIONS = (
        ('Evaluateurs', 'Evaluateurs'),
        ('Responsables de parcours', 'Responsables de parcours'),
        ('Eleves', 'Eleves'),
    )
    name = models.CharField(max_length=50, choices=FONCTIONS,default='')


    def __str__(self):
        return self.name


class Profil(models.Model):
    user = models.OneToOneField(User, related_name='profil',on_delete=models.CASCADE)
    fonctions = models.ManyToManyField(Fonction)




@receiver(m2m_changed, sender=Profil.fonctions.through)
def profil_fonction_changed(sender, instance, **kwargs):
    instance.user.groups.remove(Group.objects.get(name='Evaluateurs'))
    instance.user.groups.remove(Group.objects.get(name='Responsables de parcours'))
    instance.user.groups.remove(Group.objects.get(name='Eleves'))
    action = kwargs.pop('action', None)
    if action == "post_add":
        for fonction in instance.fonctions.all():
            group = Group.objects.get(name=fonction)
            instance.user.groups.add(group)
    if action == "post_remove":
        for fonction in instance.fonctions.all():
            group = Group.objects.get(name=fonction)
            instance.user.groups.add(group)
