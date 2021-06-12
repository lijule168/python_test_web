#!/usr/bin/python
#-*- coding:utf-8 -*-
import os, importlib

__author__ = "dingbaixia@mobike.com"

class DBAdmin:
    def __init__(self, tb_dict):
        self.class_name = list(dict(tb_dict).keys())[0]
        self.module_path = tb_dict[self.class_name].replace("/", '.')
        self.module = importlib.import_module(self.module_path)
        self.__instance = getattr(self.module, self.class_name)()

    def query(self, where_instance, *args):
        '''
        查询数据库
        :param where_instance: 查询条件（数据库表对象）
        :param args: 查询的字段
        :return:
        '''
        if where_instance is None:
            records = self.__instance.select(*args)
            return records
        else:
            records = self.__instance.where(**where_instance.__dict__).select(*args)
            return records

    def query_with_column(self, where_instance, column):
        '''
        查询数据库
        :param where_instance: 查询条件（数据库表对象）
        :param column: 查询的字段
        :return:
        '''
        columns = column.split(',')
        if where_instance is None:
            records = self.__instance.select(*tuple(columns))
            return records
        else:
            records = self.__instance.where(**where_instance.__dict__).select(*tuple(columns))
            return records

    def add_record(self, instance):
        '''
        添加数据
        :param instance: 数据对象
        :return:
        '''
        instance = getattr(self.module, self.class_name)(**instance.__dict__)
        instance.save()

    def update_record(self, where_instance, update_instance):
        '''
        更新数据
        :param where_instance: 查找需更新的数据
        :param update_instance: 更新的对象
        :return:
        '''
        if where_instance is None:
            self.__instance.update(**update_instance.__dict__)
        else:
            self.__instance.where(**where_instance.__dict__).update(**update_instance.__dict__)

    def del_record(self, where_instance):
        '''
        删除数据
        :param where_instance: 删除数据的条件
        :return:
        '''
        if where_instance is None:
            self.__instance.delete()
        else:
            self.__instance.where(**where_instance.__dict__).delete()