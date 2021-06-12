#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class MvpReq(BaseReq):
    '''
    n*n实验相关接口
    '''
    def __init__(self):
        super(MvpReq, self).__init__(micro_service_name=MicroServiceName.WECHAT)

    def get_mvp_info(self, param_dict={}):
        '''
        获取退押金后可参加活动的信息
        :param
        :return:
        '''
        return self.request("POST", "mvp/getMvpInfo", params=param_dict)

    def add_or_update_user_mvp_config(self, param_dict={}):
        '''
        用户选择试骑
        :param
        :return:
        '''
        return self.request("POST", "mvp/addOrUpdateUserMvpConfig", params=param_dict)

    def mvp_getcardcityconfig(self, param_dict=None):
        '''
        getCardCityConfig
        '''
        return self.request("GET", "mvp/getCardCityConfig", params=param_dict)

    def mvp_getusercarddeatil(self, param_dict=None):
        '''
        获取用户的 mvp礼包信息
        '''
        return self.request("POST", "mvp/getUserCardDeatil", params=param_dict)

    def mvp_buyMvp(self, param_dict=None):
        '''
        购买接口（测试用）
        :param param_dict:
        :return:
        '''
        return self.request("GET", "mvp/buyMvp", params=param_dict)