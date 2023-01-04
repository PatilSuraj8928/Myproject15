from django.urls import path
from app3.views import *
app_name = 'thirdapp'

urlpatterns = [
    path('third/',third,name='third'),
]