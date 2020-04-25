from django.contrib import admin
# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *
from .forms import *

# Define an inline admin descriptor for Eleve model
# which acts a bit like a singleton
class ProfilInline(admin.StackedInline):
    model = Profil
    form = ProfilForm
    can_delete = False
    verbose_name_plural = 'profil'


@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
    pass

# Define a new User admin

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilInline,)
    list_display = ('username','groupe', )

    def groupe(self, obj):

        return ' , '.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
