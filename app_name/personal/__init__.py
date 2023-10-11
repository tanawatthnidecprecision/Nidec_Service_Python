# app_name/personal/positionControl.py
from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from app_name.handleRequest import *
from django.db import connection, connections

import hashlib
import json
import random


class positionControl(APIView,handleEvent):

    def post(self, request):
        print('w')
        handleEvent.handleToken(request)
        if(request.POST['user_index']):
            print('a')
            sql_query = "select * from position_control where user_index = %s"
            with connections['user_lists'].cursor() as cursor:
                cursor.execute(sql_query, [request.POST['user_index']])
                results = cursor.fetchall()

            status_results = {}
            if handleEvent.handleResults(results):
                status_results['status'] = results
            else:
                status_results['status'] = 'none'
            tmp =  status.HTTP_200_OK if status_results['status'] != "none" else status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response(status_results,status=tmp)