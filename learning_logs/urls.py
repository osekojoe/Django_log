'''Defines URL logs for learning_logs'''
from django.urls import path
from . import views 

app_name = 'learning_logs'
urlpatterns = [
     #Home
     path('', views.index, name = 'index')
]
