# app_name/urls.py

from django.urls import path
from .views import *
from .user_list import *

urlpatterns = [
    # API 
    path('authentication/', Login.as_view(), name='login'),
    path('department/',Department.as_view(), name='department'),
    path('picture_list/',PictureList.as_view(), name='picture_list'),
    path('notify_intranets/',NotifyIntranets.as_view(), name="notify_intranets"),
    
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    
    path('logout/', Logout.as_view(), name='logout'),
]


    #path('login/', Login.as_view(), name='login'),

    #path('get_position_user_list/', Position.as_view(), name='get_position_user_list'),
    #path('get_position_level_user_list/', PositionLevel.as_view(), name='get_position_level_user_list'),
    #path('get_department_control/', DepartmentControl.as_view(), name='get_department_control'),

    # API Service 
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #path('fake/', FakeAPI.as_view(), name='picture_profile'),
    #
    #path('logout/', Logout.as_view(), name='logout'),