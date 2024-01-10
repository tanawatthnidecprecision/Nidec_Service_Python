from rest_framework import generics, permissions
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import connection, connections


class DatabasePagination():
    def __init__(self, type_list, database_name='setting_systems', table_name='approve_alarm'):
        self.table = table_name
        self.type_list = type_list
        self.database_name = database_name

    def getSkip(self, user_index, skip, limit, read):
        sql_query = "SELECT * from {} LEFT JOIN type_list ON approve_alarm.type_index = type_list.type_index WHERE {}.type_index IN ({}) AND user_index = {} {} order by date_alarm DESC LIMIT {} OFFSET {}".format(
            self.table, self.table, ",".join([str(i) for i in self.type_list]), user_index,('' if read == '-1' else 'AND read = '+read), limit, skip)
        print('>>',read,'' if read == -1 else 'AND read = '+read)
        print(sql_query)
        print()
        if (self.table == "approve_alarm"):
            sql_query = f"""

            SELECT DISTINCT approve_alarm.*,approve.num,approve_flow.num,approve_sec.num,approve.slip_index,type_list.type_name,type_list.link_disp
            from approve_alarm
            LEFT JOIN approve
            ON approve_alarm.slip_index = approve.slip_index
            AND approve_alarm.date_alarm = approve.app_date
            LEFT JOIN (
            select (max(num))as num,slip_index,type_index
            from approve_flow
            group by slip_index,type_index
            )approve_flow
            ON approve_alarm.slip_index = approve_flow.slip_index
            AND approve_alarm.type_index = approve_flow.type_index
            LEFT JOIN
            (
            select (max(num))as num,slip_index,type_index
            from approve_sec
            group by slip_index,type_index
            )approve_sec
            ON approve_sec.slip_index = approve_flow.slip_index
            AND approve_sec.type_index = approve_flow.type_index
            LEFT JOIN type_list on type_list.type_index = approve_alarm.type_index


            WHERE approve_alarm.type_index IN ({",".join(map(str, self.type_list))})
            AND approve_alarm.user_index = {user_index}
            order by date_alarm
            LIMIT {limit}
            OFFSET {skip}
            """
        print(sql_query)
        with connections[self.database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results

    def getCount(self, user_index,read):
        sql_query = "SELECT COUNT(*) from {} WHERE {}.type_index IN ({}) AND user_index = {}".format(
            self.table, self.table, ",".join([str(i) for i in self.type_list]), user_index)
        sql_query += '' if read == '-1' else ' AND read =' + read
        print('get count:',sql_query)
        with connections[self.database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results[0]


class DatabaseQuery():
    def selectWhere(table_name, select, query, database_name='user_lists'):
        sql_query = "select {} from {} where {}".format(
            select, table_name, query)
        print("->", sql_query, database_name)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results


class Database():
    def selectLimit(table_name, select, query_key, query_value, limit, order_by, sort, database_name='user_lists'):
        sql_query = 'select {} from \"{}\" where {} = \'{}\' order by {} {} limit {}'.format(
            select, table_name, query_key, query_value, order_by, sort,  limit)
        print(sql_query)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results

    def selectWhere(table_name, select, query_key, query_value, database_name='user_lists'):
        sql_query = 'select {} from \"{}\" where \"{}\" {} {}'.format(
            select, table_name, query_key.replace("$like", ""), "like" if "$like" in query_key else "=", "\'%"+query_value+"%\'" if "$like" in query_key else (query_value if isinstance(query_value, int) else "\'{}\'".format(query_value)))
        print(sql_query)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results

    def insert(table_name, columns, values, database_name='user_lists', returning='*'):
        with connections[database_name].cursor() as cursor:
            print(values)
            placeholders = ', '.join(['%s' if str(value).replace(
                '.', '', 1).isdigit() else '%s' for value in values])
            columns_str = ', '.join(columns)
            sql_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders}) RETURNING {returning}"
            print(sql_query, list(values))
            cursor.execute(sql_query, list(values))
            results = cursor.fetchall()
        return results

    def update(table_name, json_temp, condition, database_name='user_lists'):
        print('111>>', condition)
        print('-------', json_temp)
        formatted_data = ""
        for key, value in json_temp.items():
            print(key, value)
            if type(value) == type([]):
                if(''.join(value).replace(' ','') != ''):
                    formatted_data += "\""+key + "\"=\'" + ','.join(map(str, value)) + "\',"
            elif isinstance(value, int):
                formatted_data += "\""+key + "\"=" + str(value) +","
            elif str(value) != 'None':
                formatted_data += "\"" + key + "\"=\'" + str(value) + "\',"
        formatted_data = formatted_data[:-1]
        formatted_data += " "
        print(">"+formatted_data+"<")
        print('22>>')
        sql_query = "update \"{}\" set {} where {} returning *".format(
            table_name, formatted_data, condition)
        print(sql_query)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results

    def delete(table_name, condition, database_name='user_lists'):
        sql_query = "delete from \"{}\" where {} returning *".format(
            table_name, condition)
        print(sql_query)
        with connections[database_name].cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        return results
