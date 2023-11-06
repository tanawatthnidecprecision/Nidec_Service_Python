# app_name/views.py
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class Approve(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        value = Database.insert('approve_process', [
                                'user_index',
                                'type_index',
                                'department_index',
                                'slip_index'],
                                [
                                    int(request.data['user_index']),
                                    int(request.data['type_index']),
                                    int(request.data['department_index']),
                                    int(request.data['slip_index'])
        ], 'slip')
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        value = Database.selectWhere(
            'approve_process', '*', request.GET['query_key'], request.GET['query_value'], 'slip')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)


class ApproveFlow(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            if request.data['method'] == 'update':
                jsonTemp = request.data.get('data', {})
                pamary_key = request.data.get('approve_process_flow_id', None)
                if pamary_key == None:
                    return pamary_key
                condition = "{} = {}".format('approve_process_flow_id',pamary_key)
                results = Database.update('approve_process_flow', jsonTemp, condition, 'slip')
                return JsonResponse({'status': 'successful', 'data': results}, safe=False)
            else:
                raise Exception("ไม่มีข้อมูลเพื่อทำการอัปเดต")
        except:
            value = Database.insert('approve_process_flow', [
                                    'approve_process_id',
                                    'approve_json'],
                                    [
                                        int(request.data['approve_process_id']),
                                        (request.data['approve_json'])
            ], 'slip')
            return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        value = Database.selectWhere(
            'approve_process_flow', '*', request.GET['query_key'], request.GET['query_value'], 'slip')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)
