#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class UserApplicationReq(BaseReq):
    def __init__(self):
        super(UserApplicationReq, self).__init__() # micro_service_name=MicroServiceName.ORTHRUS_BASICINFO

    def userapplication_opencarcode(self, param_dict=None, header_dict=None):
        '''
        开通乘车码业务
        '''
        return self.request("GET", "api/orthrus/orthrus-basicinfo/userApplication/openCarCode", params=param_dict, headers=header_dict)

    def userapplication_opennooauthpay(self, param_dict=None, header_dict=None):
        '''
        开通微信免密
        '''
        return self.request("GET", "api/orthrus/orthrus-basicinfo/userApplication/openNoOauthPay", params=param_dict, headers=header_dict)

