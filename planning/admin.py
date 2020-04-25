from django.contrib import admin

from .models import *

# Register your models here.



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
