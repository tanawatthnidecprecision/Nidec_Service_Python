# app_name/views.py
from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection, connections

import hashlib
import json
import random
from app_name.handleRequest import *
from app_name.database import *

# views.py

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileUploadSerializer
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print('tt')
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']

            # บันทึกไฟล์ลงในเซิร์ฟเวอร์ (ในที่นี้ใช้ FileSystemStorage)
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)

            # สร้าง URL สำหรับไฟล์ที่บันทึกลงในเซิร์ฟเวอร์
            file_url = fs.url(filename)

            return Response({'message': 'ไฟล์ถูกอัปโหลดเรียบร้อย', 'file_url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):   
        rule = "user_list.id = '{}' and user_list.password = '{}'".format(request.POST['name'], hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest().upper())  
        results = Database.selectWhere('user_list','user_index',rule)
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
        request.session.save()
        tmp =  status.HTTP_200_OK if status_results['status'] != "Login Invalid" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(status_results,status=tmp)


class Logout(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        request.session['login'] = "";
        return Response({'status': 'successfl logout'},status=status.HTTP_200_OK)
    


