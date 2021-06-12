import datetime
import json

from lib.mbmanage.dbmanage.db_admin import DBAdmin
from lib.util.log_util import l

__author__ = "dingbaixia@mobike.com"

class DBBusiness(object):
    def __init__(self, tb_dict):
        self.__instance = DBAdmin(tb_dict=tb_dict)

    def query(self, where_instance, *args):
        '''
        查询数据库
        :param where_instance: 查询条件（数据库表对象）
        :param args: 查询的字段
        :return:
        '''
        records = self.__instance.query(where_instance, *args)
        return records

    def query_with_column(self, where_instance, column):
        '''
        查询数据库
        :param where_instance: 查询条件（数据库表对象）
        :param column: 查询的字段
        :return:
        '''
        records = self.__instance.query_with_column(where_instance, column)
        return records

    def add_record(self, instance):
        '''
        添加数据
        :param instance: 数据对象
        :return:
        '''
        self.__instance.add_record(instance)

    def update_record(self, where_instance, update_instance):
        '''
        更新数据
        :param where_instance: 查找需更新的数据
        :param update_instance: 更新的对象
        :return:
        '''
        self.__instance.update_record(where_instance=where_instance, update_instance=update_instance)

    def del_record(self, where_instance):
        '''
        删除数据
        :param where_instance: 删除数据的条件
        :return:
        '''
        self.__instance.del_record(where_instance=where_instance)

    def convert_to_dict(self, select_columns, query_result):
        """
        sql查询结果转化为字典
        :param select_columns:
        :param query_result:
        :return:
        """
        dict_obj = {}
        i = 0
        for column in select_columns.split(','):
            print(column)
            item_value = query_result[i]
            if isinstance(item_value, datetime.datetime):
                item_value = item_value.strftime('%Y-%m-%d %H:%M:%S')
            if isinstance(item_value, datetime.date):
                item_value = item_value.strftime('%Y-%m-%d')
            dict_obj[column] = item_value
            i = i + 1

        return dict_obj

    def convert_dict_to_obj(self, obj_dict, dest_obj):
        """
        字典转化为对象
        :param dict_obj:
        :param dest_obj:
        :return:
        """
        try:
            json_dumps = json.dumps(obj_dict)
            json.loads(json_dumps, object_hook=dest_obj.to_object)
        except Exception as ex:
            l.error("字典转化为对象失败，dict:{0}, dest_obj:{1}".format(obj_dict, dest_obj))
            return None


