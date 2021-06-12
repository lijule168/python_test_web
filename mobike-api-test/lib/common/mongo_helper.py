#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "dingbaixia@mobike.com"

import pymongo
from lib.util.log_util import l

class MongoDBHelper(object):
    def __init__(self, user_name, passwd, host, db_name, collection, port=27017):
        try:
            l.info("init mongodb connect: host(%s), port(%s), user_name(%s), passwd(%s)" % (host,
                port, user_name, passwd))
            if passwd:
                mongo_url = "mongodb://%s:%s@%s/" % (user_name, passwd, host)
                self.client = pymongo.MongoClient(mongo_url)
            else:
                self.client = pymongo.MongoClient(host=host, port=port)
            self.db = self.client.get_database(db_name)
            self.collection = self.db.get_collection(collection)
        except Exception as ex:
            l.error("init mongodb conn failed, Exception: %s" % (ex))

    def __close_conn(self):
        l.info("close mongodb connection")
        if self.client:
            self.client.close()

    def insert_record(self, record_dict={}):
        '''
        向mongodb中插入数据
        :param record_dict:
        :return:
        '''
        try:
            l.info("insert data to mongodb:%s" % record_dict)
            result = self.collection.insert_one(record_dict)
            return result
        except Exception as ex:
            l.error("inert data to mongodb failed, Error message:%s" % ex)
        finally:
            self.__close_conn()

    def update_record(self, where_dict, update_dict):
        '''
        更新mongodb中的数据
        :param where_dict:
        :param update_dict:
        :return:
        '''
        try:
            l.info("update data to mongodb:where(%s), update(%s)" % (where_dict, update_dict))
            result = self.collection.update_one(filter=where_dict, update=update_dict)
            return result
        except Exception as ex:
            l.error("update data to mongodb failed, Error message:%s" % ex)
        finally:
            self.__close_conn()

    def query_record(self, query_dict):
        '''
        从mongodb中取数据
        :param query_dict:
        :return:
        '''
        try:
            l.info("update data to mongodb:query(%s))" % (query_dict))
            result = self.collection.find_one(filter=query_dict)
            return result
        except Exception as ex:
            l.error("query data from mongodb failed, Error message:%s" % ex)
        finally:
            self.__close_conn()

    def del_record(self, where_dict):
        '''
        删除mongodb中的数据
        :param where_dict:
        :return:
        '''
        try:
            l.info("update data to mongodb:where(%s)" % (where_dict))
            result = self.collection.delete_many(filter=where_dict)
            return result
        except Exception as ex:
            l.error("del mongodb data failed, Error message:%s" % ex)
        finally:
            self.__close_conn()

    def update_one(self, where_dict, update_dict):
        '''
        更新一条mongodb中的数据
        :param where_dict:
        :param update_dict:
        :return:
        '''
        try:
            l.info("update data to mongodb:where(%s), update(%s)" % (where_dict, update_dict))
            result = self.collection.update_one(filter=where_dict, update=update_dict)
            return result
        except Exception as ex:
            l.error("update data to mongodb failed, Error message:%s" % ex)
        finally:
            self.__close_conn()