#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class MessageReq(BaseReq):
    #发送物联网短信
    UPLINEK_MSG = "api/v2/uplinkMsg.do"

    def __init__(self):
        super(MessageReq, self).__init__()

    def uplinkMsg(self, param_dict={}, header_dict={}):
        '''
        发送物联网短信
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", MessageReq.UPLINEK_MSG, params=param_dict, headers=header_dict)


