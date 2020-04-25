from django.urls import path
from . import views

app_name = 'evaluation'

urlpatterns = [
    path('event/<event_id>/', views.evaluation_new, name='event_evaluate'),
    path('index/', views.index, name='index'),
]
