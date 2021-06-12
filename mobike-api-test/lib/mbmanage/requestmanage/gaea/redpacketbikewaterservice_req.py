#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

import json

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class RedPacketBikeWaterReq(BaseReq):
    #插入待领取红包
    INSERT_REDPACKETWATER = "gaea/redPacket/water/insertRedPacketWater"
    #查看红包信息
    QUERY_REDPACEKETINFO = "gaea/redPacket/water/queryRedPacketInfo"
    #查看红包信息
    FIND_REDPACKETINFO = "gaea/redPacket/water/findRedPacketInfo"
    #领取红包
    RETRIEVE_REDPACKET = "gaea/redPacket/water/retrieveRp"
    #红包翻倍
    SHARE_REDPAXKET = "gaea/redPacket/water/shareRp"
    #有了经纬度后给用户发红包
    GIVE_REDPACKET_RETURN_PACKETINFO = "gaea/redPacket/water/giveRedPacketInGaea"
    #有了经纬度后给用户发红包
    GIVE_REDPACKET_RETURN_WATER = "gaea/redPacket/water/giveRedPacketInGaeaReturnMBKWater"

    def __init__(self):
        super(RedPacketBikeWaterReq, self).__init__(micro_service_name=MicroServiceName.GAEA)

    def insertRedPacketWater(self, param_dict, json_dict):
        '''
        插入待领取红包
        :param param_dict:
        :param json_dict:
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = RedPacketBikeWaterReq.INSERT_REDPACKETWATER + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def queryRedPacketInfo(self, param_dict):
        '''
        查看红包信息
        :param param_dict:
        :param json_dict:
        :return:
        '''
        return self.request("POST", RedPacketBikeWaterReq.QUERY_REDPACEKETINFO, params=param_dict)

    def findRedPacketInfo(self, param_dict):
        '''
        查看红包信息
        :param param_dict:
        :param json_dict:
        :return:
        '''
        return self.request("POST", RedPacketBikeWaterReq.FIND_REDPACKETINFO,params=param_dict)

    def retrieve_redpacket(self, param_dict):
        '''
        领取红包
        :param param_dict:
        :param json_dict:
        :return:
        '''
        return self.request("POST", RedPacketBikeWaterReq.RETRIEVE_REDPACKET, params=param_dict)

    def shareRp(self, param_dict):
        '''
        红包翻倍
        :param param_dict:
        :param json_dict:
        :return:
        '''
        return self.request("POST", RedPacketBikeWaterReq.SHARE_REDPAXKET, params=param_dict)

    def giveRedPacketInGaea(self, param_dict, json_dict):
        '''
        有了经纬度后给用户发红包
        :param param_dict:
        :param json_dict:
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = RedPacketBikeWaterReq.GIVE_REDPACKET_RETURN_PACKETINFO + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def giveRedPacketInGaeaReturnMBKWater(self, param_dict, json_dict):
        '''
        有了经纬度后给用户发红包
        :param param_dict:
        :param json_dict:
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = RedPacketBikeWaterReq.GIVE_REDPACKET_RETURN_WATER + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)