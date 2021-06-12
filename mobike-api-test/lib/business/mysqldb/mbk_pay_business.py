#!/usr/bin/python
#-*- decoding:utf-8 -*-

__author__ = "dingbaixia@mobike.com"

from lib.business.base_business import BaseBusiness
from lib.mbmanage.dbmanage.mbk_pay_admin import MBKPayDBAdmin

class MBKPayBusiness:
    def __init__(self):
        self.__instance = MBKPayDBAdmin()

    def insert_balance(self, user_id, balance, mobile=None):
        '''
        充值余额
        :param fee：充值余额
        :param user_id: 用户ID
        :return:
        '''
        self.__instance.delete_balance(userid=user_id)
        records = self.__instance.insert_balance(user_id=user_id, fee=balance, mobileno=mobile)
        return records

    def update_user_balance(self, user_id, balance):
        '''
        更新用户余额
        :param user_id:
        :param balance:
        :return:
        '''
        return self.__instance.update_balance(user_id=user_id, fee=balance)

    def select_balance(self, user_id):
        '''
        查询用户余额
        :param user_id:
        :param balance:
        :return:
        '''
        balance = self.__instance.select_balance(user_id=user_id)
        return balance

    def delete_balance(self ,userid ):
        '''

        :param userid:
        :return:
        '''
        balance = self.__instance.delete_balance(userid =userid )
        return  balance