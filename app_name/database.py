from rest_framework import generics, permissions
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection, connections


class Database():
    def selectWhere(table_name, select, condition, value):
        sql_query = "select {} from {} where {} = %s".format(select,table_name, condition)
        print(sql_query)
        with connections['user_lists'].cursor() as cursor:
            cursor.execute(sql_query,[value])
            results = cursor.fetchall()
        return results
