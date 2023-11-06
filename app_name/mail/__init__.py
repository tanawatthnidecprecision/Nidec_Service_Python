from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *


class Mail(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        print('>>')
        send_mail(
            "Subject here",
            "Here is the message.",
            "auth@nidec-precision.co.th",
            ["tanawat-th@nidec-precision.co.th"],
            fail_silently=False,
        )
        return JsonResponse({'status': 'successful'}, safe=False)
