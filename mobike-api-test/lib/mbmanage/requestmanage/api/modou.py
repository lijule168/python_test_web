#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class ModouReq(BaseReq):
    #拯救蝴蝶接口
    ADD_BUTTERFLY = "api/v2/modou/addButterfly"
    #获取用户积分
    MODOU_TOTAL = "api/v2/modou/modouTotal"


    def __init__(self):
        super(ModouReq, self).__init__()

    def add_butterfly(self, param_dict={}):
        '''
        拯救蝴蝶接口
        :param param_dict:
        * @param token 用户id：兑吧商城中的为AES加密后的userId； h5中传登录后的userId
     * @param cityCode
     * @param butterflyId
     * @param source 0:兑吧商城 1:微信  2:app
     * @param description
        :return:
        '''
        return self.request("POST", ModouReq.ADD_BUTTERFLY, params=param_dict)

    def get_total_modou(self, param_dict={}):
        '''
        获取用户积分
        :param param_dict:accesstoken(通过token获取userid)
        :return:
        '''
        return self.request("GET", ModouReq.MODOU_TOTAL, params=param_dict)