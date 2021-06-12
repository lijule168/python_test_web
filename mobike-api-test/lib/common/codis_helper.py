#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

from lib.common.config_helper import EnvConfig
from lib.util.log_util import l


class CodisHelper(object):
    '''
    redis管理
    '''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(CodisHelper,cls).__new__(cls, *args, **kwargs)
            cls.__instance.__init_conn()
        return cls.__instance

    def __init_conn(self):
        codis_config = EnvConfig().mobike_codis_service
        try:
            l.info("init redis connection,(%s)"  % (codis_config.__str__()))
            pool = redis.ConnectionPool(host=codis_config.host, port=codis_config.port, db=0, password=codis_config.passwd)
            self.__codis_conn = redis.Redis(connection_pool=pool)
        except Exception as ex:
            l.error("inital redis connection failed, exception:%s" % (ex))
            raise ex

    def del_data(self, key):
        l.info("delete redis cache:key{%s}" % key)
        return self.__codis_conn.delete(key)

    def get_data(self, key):
        l.info("获取redis中的键值,key(%s)" % (key))
        return self.__codis_conn.get(key)

    def get_all_hash_subkey(self, primary_key):
        #l.info("获取hash key(%s)下所有的subkey" % primary_key)
        return self.__codis_conn.hgetall(primary_key)

    def set_data(self, key, value):
        l.info("在redis中设置键值,(key:%s, value:%s)" % (key, value))
        return self.__codis_conn.set(key, value)

    def is_exist(self, key):
        l.info("redis中是否存在key(%s)" % key)
        self.__codis_conn.exists(key)

    def set_hash_data(self,key ,sub_key, sub_value):
        return self.__codis_conn.hset(key, sub_key, sub_value)

    def del_sub_key(self, key, sub_key):
        l.info("删除subkey, key(%s), subkey(%s)" % (key, sub_key))
        return self.__codis_conn.hdel(key, sub_key)
    def set_rpush(self, key, *value):
        # l.info("设置值, key(%s), value(%s)" % (key, value))
        return self.__codis_conn.rpush(key, *value)

    def publish(self, channel, msg):
        '''
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.
        :param channel:
        :param msg:
        :return:
        '''
        l.info("publish message(%s) on channel(%s)" % (msg, channel))
        try:
            return self.__codis_conn.publish(channel=channel, message=msg)
        except Exception as ex:
            l.error(ex)
            return None
