# app_name/views.py
from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import hashlib
from django.db import connection, connections

class Temp(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        sql_query = "SELECT * FROM user_status"
        #print(request.session['a'])
        #request.session['a'] = 'a'
        with connections['user_lists'].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        token = hashlib.sha256("a".encode('utf-8')).hexdigest()
        return Response({'status':results, 'token':token},status=status.HTTP_200_OK)
    

