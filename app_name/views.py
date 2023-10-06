# app_name/views.py
from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection, connections

import hashlib
import json

class Temp(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        status_results = {}
        print(request.session['login'])
        try:
            if request.session['login'] and len(request.session['login']) > 0:
                status_results['status'] = 'successful'
            else:
                status_results['status'] = 'you don\'t have permission'
                request.session['login'] = ""
        except:
            status_results['status'] = 'you don\'t have permission'
            request.session['login'] = ""
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)
    
class ImageProfile(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        try:
            if request.session['login'] and len(request.session['login']) > 0:
                sql_query = "select pic from picture_list where picture_list.user_index = %s"
                with connections['user_lists'].cursor() as cursor:
                    cursor.execute(sql_query, [request.session['login'][0][0]])
                    results = cursor.fetchall()
                status_results['status'] = results
            else:
                status_results['status'] = 'not found image'
                request.session['login'] = ""
        except:
            status_results['status'] = 'you don\'t have permission'
            request.session['login'] = ""
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)


class Login(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        
        sql_query = "select user_index from user_list where user_list.id = %s and user_list.password = %s"
        with connections['user_lists'].cursor() as cursor:
            cursor.execute(sql_query, [request.POST['name'], hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest().upper()])

            results = cursor.fetchall()
        
        status_results = {}

        if len(results) > 0 and results:
            
            status_results['status'] = results
            request.session['login'] = results
        else:
            status_results['status'] = 'Login Invalid'
            request.session['login'] = ""
            
        
        tmp =  status.HTTP_200_OK if status_results['status'] != "Login Invalid" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)


class Logout(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        request.session['login'] = "";
        return Response({'status': 'successfl logout'},status=status.HTTP_200_OK)