#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class UserReportReq(BaseReq):
    def __init__(self):
        super(UserReportReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def userreport(self , param_dict=None):
        '''
        用户报障
        '''
        return self.request("POST", "reportFault/userReport", params=param_dict)

