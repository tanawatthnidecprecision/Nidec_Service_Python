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
import os
# views.py
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import exception_handler

from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']
            fs = FileSystemStorage()
            token = str(random.randint(0,10))
            token += str(random.randint(0,10))
            token += str(random.randint(0,10))
            token += str(random.randint(0, 10))
            hashGenerate = hashlib.sha256(("FILES"+token).encode('utf-8')).hexdigest().upper()
            filename = fs.save(hashGenerate + '.' + uploaded_file.name.split('.')[len(uploaded_file.name.split('.'))-1], uploaded_file)
            file_url = fs.url(filename)
            return Response({'data':str(file_url)},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        file_url = request.GET['image']
        file = open(settings.MEDIA_ROOT+'\\'+file_url.replace('/','\\'), 'rb')
        response = FileResponse(file)
        return response
