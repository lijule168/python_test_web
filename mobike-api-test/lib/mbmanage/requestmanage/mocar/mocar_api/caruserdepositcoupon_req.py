#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarUserDepositCouponReq(BaseReq):
    def __init__(self):
        super(CarUserDepositCouponReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def exchange(self, param_dict=None):
        '''
        兑换免押金券,  httpMethod = POST 
code:
0: OK
2: 参数不正确
500: 服务器异常
42001: 券不存在或者已经领取过了
42002: 用户有仍在生效中的券
42003: 用户已经交过押金,无法使用免押金券
42004: 用户正在退款流程中,无法使用免押金券
        '''
        return self.request("POST", "coupon/deposit/exchange", params=param_dict)

