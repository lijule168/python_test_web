#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class PacketConfigReq(BaseReq):
    #获取红包车配置
    CONFIG_GETREDPACKETCONFIG_BY_VERSION = "gaea/config/getRedPacketConfigByVersion"
    #获取红包车配置
    CONFIG_GETREDPACKETCONFIG = "gaea/config/getRedPacketConfig"

    def __init__(self):
        super(PacketConfigReq, self).__init__(micro_service_name=MicroServiceName.GAEA)

    def get_redpacketconfig_by_version(self, param_dict):
        '''
        获取红包车配置
        :param param_dict: key:cityCode,version
        :return:
        '''
        return self.request("GET", PacketConfigReq.CONFIG_GETREDPACKETCONFIG_BY_VERSION, params=param_dict)

    def get_redpacketconfig(self, param_dict):
        '''
        获取红包车配置
        :param param_dict:key:cityCode, platform, version
        :return:
        '''
        return self.request("GET", PacketConfigReq.CONFIG_GETREDPACKETCONFIG, params=param_dict)
