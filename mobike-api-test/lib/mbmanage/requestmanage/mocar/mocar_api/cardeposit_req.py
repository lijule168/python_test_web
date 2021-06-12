#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarDepositReq(BaseReq):
    def __init__(self):
        super(CarDepositReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def checkfordepositrefund(self , param_dict=None, header_dict=None):
        '''
        查看是否符合退押金条件   code:0 成功  500:内部异常 250:用户未登录 41000:用户不存在 41006:用户押金状态异常 41008:退押金时违章  41009:退押金时15天内有用车记录  41012:存在预约中未开锁的订单 41013:存在已开锁的订单 41014:存在未支付的订单 41015:用户未支付押金
        '''
        return self.request("POST", "deposit/checkForDepositRefund", params=param_dict, headers=header_dict)

    def confirmdodepositrefund(self , param_dict=None, header_dict=None):
        '''
        执行押金退款   code:0 成功  500:内部异常 250:用户未登录 41000:用户不存在 41006:用户押金状态异常 41008:退押金时违章  41009:退押金时20天内有用车记录  41010:退押金时有未完成的订单 40013:调用退款失败
        '''
        return self.request("POST", "deposit/confirmDoDepositRefund", params=param_dict, headers=header_dict)

    def createdepositandreturnpayid(self , param_dict=None, header_dict=None):
        '''
        创建缴纳押金,并返回给app payId  code:0 成功  500:内部异常 250:用户未登录 41000:用户不存在 41006:用户押金状态异常                                41007:缴纳押金PayId获取失败     41016:用户已支付押金
        '''
        return self.request("POST", "deposit/createDepositAndReturnPayId", params=param_dict, headers=header_dict)

