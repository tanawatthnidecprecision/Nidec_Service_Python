from rest_framework import generics, permissions  
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class handleEvent():
    def handleToken(request):
        return str(request.session.get('token')) == str(request.POST['token'])

    def handleResults(results):
        print(results)
        return results and len(results) > 0