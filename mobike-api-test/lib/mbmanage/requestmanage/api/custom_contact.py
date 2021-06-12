#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq

class CustomContactReq(BaseReq):
    #用户配置、消息等
    MSGLIST = "api/v2/custom/contact/msglist.do"
    #获取banner图片
    CONFIG = "api/v2/custom/contact/config.do"

    def __init__(self):
        super(CustomContactReq, self).__init__()

    def msglist(self, param_dict={}):
        '''
        消息列表
        :param param_dict:
        * @param city_code    所在城市
        * @param last_time   : 截止时间
        :return:
        '''
        return self.request("POST", CustomContactReq.MSGLIST, params=param_dict)

    def config(self, param_dict={}, header_dict={}):
        '''
        获取banner图片
        :param param_dict:
        * @param city_code    所在城市
        * @param screen_width    屏幕宽度
        :return:
        '''
        return self.request("POST", CustomContactReq.CONFIG, params=param_dict, headers=header_dict)