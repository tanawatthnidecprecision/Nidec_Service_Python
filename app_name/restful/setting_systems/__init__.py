# app_name/views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json

class routerPath(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        value = Database.selectLimit('router_intranets','*',1000,'setting_systems')
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
    
