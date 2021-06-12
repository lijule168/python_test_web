#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class RedPacketReq(BaseReq):
    #根据citycode获取红包配置信息
    GET_REDPACKETCONFIG_BY_CITYCODE = "gaea/getRedPacketConfigByCityCode"
    #更新或添加红包配置
    UPDATE_REDPACKETCONFIG = "gaea/updateRedPacketConfig"
    #删除红包配置
    DEL_REDPACKETCONFIG = "gaea/deleteConfig"

    def __init__(self):
        super(RedPacketReq, self).__init__(micro_service_name=MicroServiceName.GAEA)

    def getRedPacketConfigByCityCode(self, param_dict={}):
        '''
        获取城市红包配置信息
        :param param_dict: key:cityCode
        :return:
        '''

        return self.request("GET", api_path=RedPacketReq.GET_REDPACKETCONFIG_BY_CITYCODE, params=param_dict)

    def updateRedPacketConfig(self, param_dict={}):
        '''
        更新城市红包配置信息
        :param param_dict: key:json
        :return:
        '''

        return self.request("GET", api_path=RedPacketReq.UPDATE_REDPACKETCONFIG, params=param_dict)

    def deleteConfig(self):
        '''
        删除红包配置
        :return:
        '''
        return self.request("GET", api_path=RedPacketReq.DEL_REDPACKETCONFIG)
