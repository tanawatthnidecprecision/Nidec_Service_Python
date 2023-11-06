# app_name/urls.py

from django.urls import path
from .views import *
from .restful.user_list_service import *
from .restful.paperless_service.claimSlip import *
from .restful.approve_service import *
from .restful.personal_service import * 
from app_name.storage import FileUploadView
from .mail import Mail

urlpatterns = [
    # API 
    path('authentication/', Login.as_view(), name='login'),
    path('department/',Department.as_view(), name='department'),
    path('picture_list/',PictureList.as_view(), name='picture_list'),
    path('notify_intranets/',NotifyIntranets.as_view(), name="notify_intranets"),
    
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('approve/', Approve.as_view(), name='approve'),
    path('approve_flow/', ApproveFlow.as_view(), name='approve_flow'),
    path('approve_flow/<int:pk>/', ApproveFlow.as_view(), name='approve_flow'),
    path('claim_slip/', ClaimSlip.as_view(), name='claim_slip'),
    
    path('info/', InfoUserList.as_view(), name='info'),
    path('name_service/', nameSearch.as_view(), name='info'),
    path('mail/', Mail.as_view(), name='claim_slip'),
    
    path('logout/', Logout.as_view(), name='logout'),

]
