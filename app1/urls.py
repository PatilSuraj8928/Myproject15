from django.urls import path
from app1.views import *
app_name = 'firstapp'

urlpatterns = [
    path('first/',first,name='first'),
]