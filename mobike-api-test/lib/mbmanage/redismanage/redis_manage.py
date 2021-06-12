#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = "dingbaixia"

from lib.common.redis_helper import RedisHelper
from lib.util.log_util import l

class RedisManage(object):
    '''
    缓存的增删改查
    '''
    def __init__(self):
        self.__redis_helper = RedisHelper()

    def get_hash_subkey_by_key_word(self, primary_key, key_word):
        l.info("find subkey according keyword")
        all_sub_keys =  self.__redis_helper.get_all_hash_subkey(primary_key)
        key_list = []
        for key in all_sub_keys.keys():
            if key.__contains__(str(key_word)):
                key_list.append(key)
        return  key_list

    def del_primary_key(self, key):
        return self.__redis_helper.del_data(key)

    def set(self,key, value):
        return self.__redis_helper.set_data(key, value)

    def is_exist(self, key):
        return self.__redis_helper.is_exist(key)

    def get_key(self, key):
        return self.__redis_helper.get_data(key)

    def del_hash_subkey(self, primary_key, sub_key):
        return self.__redis_helper.del_sub_key(primary_key, sub_key)

    def set_hash_data(self, key, sub_key, sub_value):
        return  self.__redis_helper.set_hash_data(key,sub_key,sub_value)

    def set_rpush(self,key,*value):
        return self.__redis_helper.set_rpush(key, *value)

    def get_list_len(self, key):
        return self.__redis_helper.llen(key)

    def get_list_index(self, key, index):
        return self.__redis_helper.l_index(key, index)

    def list_remove_and_return_firstitem(self, key):
        """
        Remove and return first item
        :param key:
        :return:
        """
        return self.__redis_helper.l_pop(key)

    def list_insert_tailitem(self, key, value):
        return self.__redis_helper.l_rpushx(key, value)

    def publish_to_channel(self, channel, msg):
        l.info("发布消息(%s) 到频道(%s)" % (msg, channel))
        return self.__redis_helper.publish(channel=channel, msg=msg)

    def get_key_expiretime(self, key):
        """
        获取key的过期时间
        :param key:
        :return:
        """
        return self.__redis_helper.get_key_expiretime(key)
