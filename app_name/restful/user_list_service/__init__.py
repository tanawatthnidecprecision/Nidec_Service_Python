# app_name/views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json

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

class InfoUserList(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        tmp = 'user_index = \'{}\''.format(request.data['user_index'])
        print('aaaa',tmp)
        value = DatabaseQuery.selectWhere('user_list','*',tmp)[0]
        print(value)
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)
    
    def get(self, request):
        value = ""
        print('1')
        try:
            if(request.GET['query_raw']):
                print('11')
                value = DatabaseQuery.selectWhere(
                    'user_list', '*', request.GET['query_raw'])[0]
            else:
                print('111')
                raise('exception')
        except:
            print('00')
            val = request.GET['query_value'];value = DatabaseQuery.selectWhere('user_list','*','user_index = \'{}\''.format(val))[0]
        return JsonResponse({'status':'successful','data': value} if value != "" else {'status':'error'}, safe=False)


class PictureList(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = ""
        if(handleEvent.handleToken(request) and request.get['user_index']):
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

class Approve(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        value = Database.insert('approve_process',[
                                'user_index',
	                            'type_index',
                                'department_index',
	                            'slip_index'],
                                [
                                    request.POST['user_index'],
                                    request.POST['type_index'],
                                    request.POST['department_index'],
                                    request.POST['slip_index']
                                ],'slip','approve_process_id')[0][0]
        return JsonResponse({'status':'successful','data': value}, safe=False)



