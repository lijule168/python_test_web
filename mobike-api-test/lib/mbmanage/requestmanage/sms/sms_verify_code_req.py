#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class SMSVerifyCodeReq(BaseReq):
    #aliyun短信验证码
    ALIYUN_SENDCODE = "sms/verify/sendCode"
    #内部获取短信验证码
    INTERNAL_SMSCODE = "sms/verify/internal/set"

    def __init__(self):
        super(SMSVerifyCodeReq, self).__init__(micro_service_name=MicroServiceName.SMS)

    def sendCodeAliyun(self, param_dict={}, header_dict={}):
        '''
        通过阿里云发送验证码
        :param param_dict: KEY(verifyBiz, mobile)
        :return:
        '''
        return self.request("GET", api_path=SMSVerifyCodeReq.ALIYUN_SENDCODE, params=param_dict, headers=header_dict)

    def internalSmsCode(self, param_dict={}, header_dict={}):
        '''
        获得验证码
        :param param_dict: KEY(verifyBiz, mobile)
        :return:
        '''
        return self.request("GET", api_path=SMSVerifyCodeReq.INTERNAL_SMSCODE, params=param_dict, headers=header_dict)