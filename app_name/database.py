from rest_framework import generics, permissions
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection, connections


class Database():
    def selectWhere(table_name, select, query, database_name = 'user_lists'):
        sql_query = "select {} from {} where {}".format(select,table_name, query)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results
