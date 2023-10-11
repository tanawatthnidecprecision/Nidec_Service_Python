# app_name/views.py
from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection, connections

import hashlib
import json
import random
from app_name.handleRequest import *
from app_name.database import *

class InfoImageProfile(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print("InfoImageProfile>>>>",request.session.get('login'),":",str(request.session.get('token')))
        print(str(request.session.get('token')), Database.selectWhere('picture_list','pic','user_index',str(request.session.get('login'))))
        status_results['status'] = 'you have permission ' + str(request.session.get('token'))
        
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)

class ImagePic(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print("ImagePic>>>>",request.session.get('login'),":",str(request.session.get('token')))
        status_results['status'] = 'you have permission ' + str(request.session.get('token'))
        
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)

class FakeAPI3(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print("FakeAPI3>>>>",request.session.get('login'),":",str(request.session.get('token')))
        status_results['status'] = 'you have permission ' + str(request.session.get('token'))
        request.session.modified = True
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)
    
class FakeAPI(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print("FakeAPI>>>>",request.session.get('login'),":",str(request.session.get('token')))
        status_results['status'] = 'you have permission ' + str(request.session.get('token'))
        request.session.modified = True
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)
    
class FakeAPI2(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print("FakeAPI2>>>>",request.session.get('login'),":",str(request.session.get('token')))
        status_results['status'] = 'you have permission ' + str(request.session.get('token'))
        request.session.modified = True
        tmp =  status.HTTP_200_OK if status_results['status'] != "you don\'t have permission" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)
    
class Position(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print(str(request.session.get('token')))
        if(request.POST['position_index'] and handleEvent.handleToken(request)):
            sql_query = "select * from position_control where position_index = %s"
            with connections['user_lists'].cursor() as cursor:
                cursor.execute(sql_query, [request.POST['position_index']])
                results = cursor.fetchall()

            status_results = {}
            #if handleEvent.handleResults(results):
            #    
            #else:
            #    status_results['status'] = 'none'
            status_results['status'] = results
            tmp =  status.HTTP_200_OK if status_results['status'] != "none" else status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response(status_results,status=tmp)
        else:
            return Response({'status':'error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PositionLevel(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print(str(request.session.get('token')))
        if(request.POST['level_code'] and handleEvent.handleToken(request)):
            sql_query = "select * from position_level where level_code = %s"
            with connections['user_lists'].cursor() as cursor:
                cursor.execute(sql_query, [request.POST['level_code']])
                results = cursor.fetchall()

            status_results = {}
            status_results['status'] = results
            tmp =  status.HTTP_200_OK if status_results['status'] != "none" else status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response(status_results,status=tmp)
        else:
            return Response({'status':'error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DepartmentControl(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        status_results = {}
        print(str(request.session.get('token')))
        if(request.POST['department_index']):
            sql_query = "select * from department_control where department_index = %s"
            with connections['user_lists'].cursor() as cursor:
                cursor.execute(sql_query, [request.POST['department_index']])
                results = cursor.fetchall()

            status_results = {}
            status_results['status'] = results
            tmp =  status.HTTP_200_OK if status_results['status'] != "none" else status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response(status_results,status=tmp)
        else:
            return Response({'status':'error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        sql_query = "select user_index from user_list where user_list.id = %s and user_list.password = %s"
        with connections['user_lists'].cursor() as cursor:
            cursor.execute(sql_query, [request.POST['name'], hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest().upper()])

            results = cursor.fetchall()
        
        status_results = {}

        if len(results) > 0 and results:
            token = str(random.randint(0,10))
            token += str(random.randint(0,10))
            token += str(random.randint(0,10))
            token += str(random.randint(0,10))
            
            status_results['status'] = 'successful'
            status_results['token'] = hashlib.sha256(("TOKEN"+str(results[0][0])+ token).encode('utf-8')).hexdigest().upper()
            request.session['login'] = results
            request.session['token'] = status_results['token']
        else:
            status_results['status'] = 'invalid'
            request.session['login'] = ""
            request.session['token'] = ""
            
        request.session.modified = True
        print("Login>>>>",request.session.get('login'),":",str(request.session.get('token')))
        tmp =  status.HTTP_200_OK if status_results['status'] != "Login Invalid" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)


class Logout(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        request.session['login'] = "";
        return Response({'status': 'successfl logout'},status=status.HTTP_200_OK)
    


