from django.urls import path
from . import views

app_name = 'evaluationtype'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('new/', views.evaluationtype_new, name='new'),
    path('new2/<pk>/', views.evaluationtype_new2, name='new2'),
]
