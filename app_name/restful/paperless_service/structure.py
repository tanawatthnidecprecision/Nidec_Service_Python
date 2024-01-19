# app_name/paperless_service/structure.py

from django.http import JsonResponse
from app_name.handleRequest import *
from app_name.database import *
import json


class Structure(APIView):
    permission_classes = [permissions.AllowAny]

    def __init__(self, table_name, pamary_key, database_name):
        self.table_name = table_name#"claim_slip_systems"
        self.pamary_key = pamary_key#"claim_slip_index"
        self.database_name = database_name#"slip"

    def get(self, request):
        try:
            if request.GET['query_where_raw'] and request.GET['query_like']:
                tmp = ""
                if(request.GET['query_value'].isdigit()):
                    tmp = "= " + request.GET['query_value']
                else:
                    tmp = "like \'%" + request.GET['query_value']+"%\'"
                print(self.table_name, '*', request.GET['query_like']+" "+ tmp + request.GET['query_where_raw'])
                value = DatabaseQuery.selectWhere(
                self.table_name, '*', request.GET['query_like']+" "+ tmp + request.GET['query_where_raw'], self.database_name)
                return JsonResponse({'status': 'successful', 'data': value}, safe=False)
        except:
            try:
                # like แบบ เงื่อนไข
                # return
                if request.GET['query_like']:
                    tmp = ""
                    if(request.GET['query_value'].isdigit()):
                        tmp = "= " + request.GET['query_value']
                    else:
                        tmp = "like \'%" + request.GET['query_value']+"%\'"
                    print('AAAA')
                    value = DatabaseQuery.selectWhere(
                    self.table_name, '*', request.GET['query_like']+" "+ tmp, self.database_name)
                    print('AAA')
                    return JsonResponse({'status': 'successful', 'data': value}, safe=False)
                else:
                    raise Exception('error')
            except:
                print('B')
                value = Database.selectWhere(
                    self.table_name, '*', request.GET['query_key'], request.GET['query_value'], self.database_name)[0]
                return JsonResponse({'status': 'successful', 'data': value}, safe=False)

    def post(self, request):
        try:
            print('A>',request.data['method'])
            if request.data['method'] == 'update':
                print('B>',request.data['method'])
                jsonTemp = request.data.get('data', {})
                pamary_key = request.data.get(self.pamary_key, None)
                if pamary_key == None:
                    return pamary_key
                condition = "{} = {}".format(self.pamary_key, pamary_key)
                print('C>',condition)
                results = Database.update(self.table_name, jsonTemp, condition, self.database_name)
                return JsonResponse({'status': 'successful', 'data': results}, safe=False)
            else:
                raise Exception('error')
        except:
            print('except')
            jsonTemp = request.data['data']
            value = Database.insert(self.table_name, jsonTemp.keys(),
                                    jsonTemp.values(), self.database_name, self.pamary_key)
            return JsonResponse({'status': 'successful', 'data': value}, safe=False)
        
        

    def patch(self, request):
        jsonTemp = request.data.get('data', {})
        pamary_key = request.data.get(self.pamary_key, None)
        if pamary_key == None:
            return pamary_key
        condition = "{} = {}".format(self.pamary_key,pamary_key)
        Database.update(self.table_name, jsonTemp, condition, self.database_name)
        return JsonResponse({'status': 'successful', 'data': 'Updated'}, safe=False)
    
    def delete(self, parameter):
        try:
            Database.selectWhere(
                self.table_name, self.pamary_key, '{} = {}'.format(self.pamary_key, self.request.data.get(self.pamary_key, None)), self.database_name)[0]
        except IndexError:
            return JsonResponse({'status': 'error', 'data': '{} not found'.format(self.request.data.get(self.pamary_key, None))}, status=status.HTTP_404_NOT_FOUND)

        condition = "{} = {}".format(self.pamary_key, self.request.data.get(self.pamary_key, None))
        Database.delete(self.table_name, condition, self.database_name)

        return JsonResponse({'status': 'successful', 'data': 'deleted'}, safe=False)

