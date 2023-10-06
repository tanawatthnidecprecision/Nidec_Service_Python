# app_name/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('temp/', Temp.as_view(), name='temp'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', ImageProfile.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
