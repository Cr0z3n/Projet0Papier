from django.contrib import admin

# Register your models here.

from .models import *

# Register your models here.

@admin.register(Critere)
class CritereAdmin(admin.ModelAdmin):
    pass

@admin.register(Champ)
class ChampAdmin(admin.ModelAdmin):
    pass
