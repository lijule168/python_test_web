#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class RedPacketConfigReq(BaseReq):
    #更新红包配置
    UPDATE_REDPACKET_CONFIG = "athena/config/redpacket/updateRedPacketConfig.do"

    def __init__(self):
        super(RedPacketConfigReq, self).__init__()

    def udpate_redpacket_config(self, json_data=None):
        '''
        更新红包配置
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type":"application/json;charset=UTF-8"}
        return self.request("POST", RedPacketConfigReq.UPDATE_REDPACKET_CONFIG, headers=header_dict, json_data=json_data)

