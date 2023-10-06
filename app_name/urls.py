# app_name/urls.py

from django.urls import path
from .views import Temp

urlpatterns = [
    path('temp/', Temp.as_view(), name='temp'),
]
