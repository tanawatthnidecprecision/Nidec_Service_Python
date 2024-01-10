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
        print('::',request.GET['permission'])
        value = Database.selectLimit('router_intranets','*', 'permission', request.GET['permission'],1000, 'super_path', 'DESC','setting_systems')
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
    
class typeList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        value = DatabaseQuery.selectWhere('type_list','*', 'type_index = '+ request.GET['type_index'],'slip_db01')
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
    
