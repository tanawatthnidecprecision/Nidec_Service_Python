# app_name/views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class Config(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        value = []
        try:
            if request.data['method'] == 'update' and request.data['condition']:
                jsonData = json.loads(request.data['data'])
                value = Database.update(request.data['table_name'],
                                        jsonData, request.data['condition'], 'user_config')
            else:
                raise ('exception')
        except:
            jsonData = json.loads(request.data['data'])
            value = Database.insert(request.data['table_name'],
                                    jsonData.keys(),
                                    jsonData.values(), 'user_config')
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        try:
            try:
                if (request.GET['query_raw'] and request.GET['query_key']):
                    value = DatabaseQuery.selectWhere(
                        request.GET['query_key'], '*', request.GET['query_raw'], 'user_config')
                else:
                    raise ('exception')
            except:
                if (request.GET['query_raw']):
                    value = DatabaseQuery.selectWhere(
                        'user_config', '*', request.GET['query_raw'], 'user_config')
                else:
                    raise ('exception')
        except:
            val = request.GET['query_value']
            value = DatabaseQuery.selectWhere(
                'user_config', '*', 'id = \'{}\''.format(val), 'user_config')
        return JsonResponse({'status': 'successful', 'data': value} if value != "" else {'status': 'error'}, safe=False)
