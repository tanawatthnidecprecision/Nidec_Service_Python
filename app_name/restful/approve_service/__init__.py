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
        ], 'slip_db01')
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        value = Database.selectWhere('approve_process', '*', request.GET['query_key'], request.GET['query_value'], 'slip_db01')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)


class ApproveFlow(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            if request.data['method'] == 'update':
                print('A')
                jsonTemp = request.data.get('data')
                condition = request.data.get('condition', None)
                print('-----------')
                print('>',jsonTemp, type(jsonTemp))
                results = Database.update('approve_process_flow', json.loads(jsonTemp), condition, 'slip_db01')
                print(results)
                return JsonResponse({'status': 'successful', 'data': results}, safe=False)
            else:
                print('error =>')
                raise Exception("ไม่มีข้อมูลเพื่อทำการอัปเดต")
        except:
            print('B')
            value = Database.insert('approve_process_flow', [
                                    'approve_process_id',
                                    'approve_json'],
                                    [
                                        int(request.data['approve_process_id']),
                                        (request.data['approve_json'])
            ], 'slip_db01')
            return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        value = Database.selectWhere(
            'approve_process_flow', '*', request.GET['query_key'], request.GET['query_value'], 'slip_db01')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)


class ApproveAlarm(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        value = Database.insert('approve_alarm', [
                                    'user_index',
                                    'slip_index',
                                    'section_name',
                                    'date_alarm',
                                    'type_index'],
                                    [
                                        int(request.data['user_index']),
                                        int(request.data['slip_index']),
                                        request.data['section_name'],
                                        'now()',
                                        int(request.data['type_index'])
            ], 'slip_db01')
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def get(self, request):
        value = Database.selectWhere(
            'approve_alarm', '*', request.GET['query_key'], request.GET['query_value'], 'slip_db01')[0]
        return JsonResponse({'status': 'successful', 'data': value}, safe=False)
