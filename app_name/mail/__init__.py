

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *


class Mail(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            send_mail(
                request.POST['title'],
                request.POST['content'],
                "auth@nidec-precision.co.th",
                [request.POST['email']],
                fail_silently=False,
            )
            return JsonResponse({'status': 'successful'}, safe=False)
        except:
            return JsonResponse({'status': 'error'}, safe=False)
        
