#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarOrderEvaluateReq(BaseReq):
    def __init__(self):
        super(CarOrderEvaluateReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def evaluate_getallstarsandtags(self, param_dict=None):
        '''
        获取订单评价星级和标签列表
        '''
        return self.request("POST", "evaluate/getAllStarsAndTags", params=param_dict)

    def evaluate_getorderevaluate(self, param_dict=None):
        '''
        查看订单评价
        '''
        return self.request("POST", "evaluate/getOrderEvaluate", params=param_dict)

    def evaluate_submitevaluate(self, param_dict=None):
        '''
        提交订单评价
        '''
        return self.request("POST", "evaluate/submitEvaluate", params=param_dict)

