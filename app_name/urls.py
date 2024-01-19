# app_name/urls.py

from django.urls import path
from .views import *
from .restful.user_list_service import *
from .restful.user_config_service import *
from .restful.paperless_service.claimSlip import *
from .restful.paperless_service.supplierName import *
from .restful.paperless_service.crudPaperless import *
from .restful.approve_service import *
from .restful.personal_service import * 
from .restful.setting_systems import *
from .pagination.setting_systems import *
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
    path('approve_alarm/', ApproveAlarm.as_view(), name='approve_flow'),
    path('claim_slip/', ClaimSlip.as_view(), name='claim_slip'),
    path('paperless/', CurdPaperless.as_view(), name='claim_slip'),
    
    path('info/', InfoUserList.as_view(), name='info'),
    path('name_service/', nameSearch.as_view(), name='info'),
    path('name_service_supplier/', supplierName.as_view(), name='info'),
    path('mail/', Mail.as_view(), name='claim_slip'),

    path('router/', routerPath.as_view(), name='router'),
    path('user_config/', Config.as_view(), name='user_config'),
    path('get_approve_alarm/', GetSystemSetting.as_view(), name='claim_slip'),
    path('skip_approve_alarm/', SkipSystemSetting.as_view(), name='claim_slip'),
    path('router/', routerPath.as_view(), name='claim_slip'),
    path('type_list/', typeList.as_view(), name='claim_slip'),
    path('logout/', Logout.as_view(), name='logout'),

]
