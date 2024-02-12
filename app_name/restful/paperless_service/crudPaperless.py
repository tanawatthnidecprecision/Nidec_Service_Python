# app_name/paperless_service/structure.py

from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class CurdPaperless(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        table_name = request.GET['table_name']
        database_name = 'slip_db01'
        try:
            if request.GET['query_where_raw'] and request.GET['query_like']:
                tmp = ""
                if(request.GET['query_value'].isdigit()):
                    tmp = "= " + request.GET['query_value']
                else:
                    tmp = "like \'%" + request.GET['query_value']+"%\'"
                value = DatabaseQuery.selectWhere(
                table_name, '*', request.GET['query_like']+" "+ tmp + request.GET['query_where_raw'], database_name)
                return JsonResponse({'status': 'successful', 'data': value}, safe=False)
        except:
            try:
                # return
                if request.GET['query_like']:
                    tmp = ""
                    if(request.GET['query_value'].isdigit()):
                        tmp = "= " + request.GET['query_value']
                    else:
                        tmp = "like \'%" + request.GET['query_value']+"%\'"
                    value = DatabaseQuery.selectWhere(
                    table_name, '*', request.GET['query_like']+" "+ tmp, database_name)
                    return JsonResponse({'status': 'successful', 'data': value}, safe=False)
                else:
                    raise Exception('error')
            except:
                print('aaa')
                value = Database.selectWhere(
                    table_name, '*', request.GET['query_key'], request.GET['query_value'], database_name)
                return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def post(self, request):
        table_name = request.data.get('table_name')
        database_name = 'slip_db01'
        try:
            if request.data['method'] == 'update':
                jsonTemp = request.data.get('data', {})
                condition = request.data.get('condition')
                results = Database.update(table_name, jsonTemp, condition, database_name)
                return JsonResponse({'status': 'successful', 'data': results}, safe=False)
            else:
                raise Exception('error')
        except:
            jsonTemp = request.data['data']
            print(jsonTemp)
            value = Database.insert(table_name, jsonTemp.keys(),
                                    jsonTemp.values(), database_name)
            return JsonResponse({'status': 'successful', 'data': value}, safe=False)
    

