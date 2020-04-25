from django.urls import path
from . import views

app_name = 'critere'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('new/', views.critere_new, name='new'),
    path('new2/<pk>/', views.critere_new2, name='new2'),
    path('champ_new/', views.champ_new, name='champ_new'),
]
