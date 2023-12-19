from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class SkipSystemSetting(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        database = DatabasePagination(request.GET['type_list'].split(','),'slip_db01')
        value = database.getSkip(request.GET['user_index'], str(request.GET['skip']), str(request.GET['limit']))
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)

class GetSystemSetting(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        database = DatabasePagination(request.GET['type_list'].split(','),'slip_db01')
        value = database.getCount(request.GET['user_index'])
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)
