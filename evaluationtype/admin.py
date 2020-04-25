from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.


@admin.register(EvaluationType)
class EvaluationTypeAdmin(admin.ModelAdmin):
    pass
