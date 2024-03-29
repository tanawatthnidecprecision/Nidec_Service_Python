# app_name/views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class Production(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        value = Database.selectWhere(request.GET['database'], '*', request.GET['query_key'], request.GET['query_value'], 'production')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)
