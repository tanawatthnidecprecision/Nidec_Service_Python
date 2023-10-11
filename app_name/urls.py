# app_name/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    # API 
    path('login/', Login.as_view(), name='login'),

    

    # API Service 
    path('fake/', FakeAPI.as_view(), name='picture_profile'),

    #  Info User
    path('fake2/',FakeAPI2.as_view(), name="picture_profile"),
    path('fake3/',FakeAPI3.as_view(), name="picture_profile"),

    path('get_position_user_list/', Position.as_view(), name='get_position_user_list'),
    path('get_position_level_user_list/', PositionLevel.as_view(), name='get_position_level_user_list'),
    path('get_department_control/', DepartmentControl.as_view(), name='get_department_control'),

    # API Service 
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #
    path('logout/', Logout.as_view(), name='logout'),
]

