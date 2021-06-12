#!/usr/bin/python
# -*- coding:utf-8 -*-

from lib.util.random_util import RandomUtil
from lib.mbmanage.dbmanage.mbk_db_admin import MBKDBDBAdmin

class UtilBusiness:
    def __init__(self):
        pass

    def get_unregister_phone(self, prefix="138", phone_len=8):
        '''
        获取没有注册过的手机号
        :param prefix:
        :param phone_len:
        :return:
        '''
        mbkdb_admin = MBKDBDBAdmin()
        is_exist = True
        i=0
        phone = None
        while is_exist and i< 1000:
            phone = RandomUtil.gen_phone_num(prefix=prefix, phone_len=phone_len)
            is_exist = mbkdb_admin.is_phone_register(phone)
            i = i + 1
        return phone