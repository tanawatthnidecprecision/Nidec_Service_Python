# app_name/views.py
from rest_framework import permissions  
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *

class Department(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = ""
        if(handleEvent.handleToken(request) and request.POST['department_index']):
            value = Database.selectWhere('department_control','*','department_index = \'{}\''.format(request.POST['department_index']))[0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)

class PositionControl(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = ""
        if(handleEvent.handleToken(request) and request.POST['department_index']):
            value = Database.selectWhere('position_control','*','position_index = \'{}\''.format(request.POST['position_index']))[0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)

class PictureList(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = ""
        if(handleEvent.handleToken(request) and request.POST['user_index']):
            print('picture_list','*','user_index = \'{}\''.format(request.POST['user_index']))
            value = Database.selectWhere('picture_list','*','user_index = \'{}\''.format(request.POST['user_index']))[0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
    
    def get(self, request):
        value = ""
        print('a')
        print(request.session.get('login'))
        if(request.session.get('login')):
            value = Database.selectWhere('picture_list','*','user_index = \'{}\''.format(request.session.get('login')[0]))[0][0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)

class NotifyIntranets(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = Database.selectWhere('approve_alarm','*','user_index = 7150','slip')[0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
