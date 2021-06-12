#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class TradeReq(BaseReq):
    def __init__(self):
        super(TradeReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_INTERNAL_API)

    def getpeccancyrecord(self, param_dict=None):
        '''
        *车辆违章备注 - 查询历史记录
        '''
        return self.request("GET", "trade/order/getPeccancyRecord.do", params=param_dict)

    def add(self, param_dict=None):
        '''
        新建计费规则
        '''
        return self.request("POST", "trade/chargeRule/add.do", params=param_dict)

    def returnpayment(self, param_dict=None):
        '''
        手动退还押金
        '''
        return self.request("POST", "trade/deposit/returnPayment.do", params=param_dict)

    def lockdoorandendorder(self, param_dict=None):
        '''
        *客服关锁结费
        '''
        return self.request("POST", "trade/order/lockDoorAndEndOrder.do", params=param_dict)

    def list(self, param_dict=None):
        '''
        查看计费规则
        '''
        return self.request("GET", "trade/chargeRule/list.do", params=param_dict)

    def detail(self, param_dict=None):
        '''
        查看用户押金详情
        '''
        return self.request("GET", "trade/deposit/detail.do", params=param_dict)

    def history(self, param_dict=None):
        '''
        查看历史订单
        '''
        return self.request("GET", "trade/order/history.do", params=param_dict)

    def paymentrecord(self, param_dict=None):
        '''
        查看押金交易记录
        '''
        return self.request("GET", "trade/deposit/paymentRecord.do", params=param_dict)

    def orderinfo(self, param_dict=None):
        '''
        *订单详情页
        '''
        return self.request("GET", "trade/order/orderInfo.do", params=param_dict)

    def changepaymentfee(self, param_dict=None):
        '''
        用户未支付订单改价
        '''
        return self.request("POST", "trade/order/changePaymentFee.do", params=param_dict)

    def checkorderstatus(self, param_dict=None):
        '''
        查询订单状态
        '''
        return self.request("GET", "trade/order/checkOrderStatus.do", params=param_dict)

    def edit(self, param_dict=None):
        '''
        编辑规则
        '''
        return self.request("POST", "trade/chargeRule/edit.do", params=param_dict)

    def editcharge(self, param_dict=None):
        '''
        编辑计费规则
        '''
        return self.request("POST", "trade/chargeRule/editCharge.do", params=param_dict)

    def addpeccancyrecord(self, param_dict=None):
        '''
        *车辆违章备注 - 新增更新
        '''
        return self.request("POST", "trade/order/addPeccancyRecord.do", params=param_dict)

    def refund(self, param_dict=None):
        '''
        用户已支付订单退款
        '''
        return self.request("POST", "trade/order/refund.do", params=param_dict)

