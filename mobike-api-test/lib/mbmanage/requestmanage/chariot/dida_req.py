#!/usr/bin/python
#-*- coding:utf-8 -*-
import time

__author__ = 'yys'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class DiDaReq(BaseReq):


    #获取嘀嗒价格配置
    DIDA_PRICECONFIG = "api/chariot/carConfig/didaPriceConfig"
    #取消订单
    DIDA_CANCEL = "api/chariot/trip/carpool/cancel"
    #取消订单原因
    DIDA_CANCEL_REASON = "api/chariot/trip/carpool/cancelreason"
    # 查询拼友状态
    DIDA_COMPANION = "api/chariot/trip/carpool/companion"
    #创建订单
    DIDA_CREATE = "api/chariot/trip/carpool/create"
    #确认搭乘
    DIDA_CONFIRM = "api/chariot/trip/carpool/confirm"
    #支付订单
    DIDA_PAYMENT = "api/chariot/trip/carpool/payment"
    #估价
    DIDA_PRICE = "api/chariot/trip/carpool/price"
    #增加感谢费
    DIDA_THANKSFEE = "api/chariot/trip/carpool/thanksfee"

    def __init__(self):
        super(DiDaReq, self).__init__()

    def dida_priceconfig(self, param_dict={}):

        return self.request("GET", DiDaReq.DIDA_PRICECONFIG, params=param_dict)
    def dida_cancel(self, param_dict = {}, header_dict ={}):
        '''
        取消订单
        :param header_dict: orderId
        :param param_dict:key:accesstoken
        :return:
        '''
        return self.request("POST", DiDaReq.DIDA_CANCEL, params=param_dict, headers=header_dict)

    def dida_cancel_reason(self, param_dict={}):

        return self.request("GET", DiDaReq.DIDA_CANCEL_REASON, params=param_dict)
    def dida_companion(self,param_dict={},header_dict = {}):

        return self.request("POST", DiDaReq.DIDA_COMPANION ,params=param_dict ,headers=header_dict)
    def dida_create(self, param_dict={}, header_dict={}):
        '''
        创建订单
        :param header_dict: citycode,version,os,platform
        :param param_dict:key:
        :return:
        '''
        time.sleep(2)
        return self.request("POST", DiDaReq.DIDA_CREATE, params=param_dict, headers=header_dict)
    def dida_confirm(self, param_dict={}, header_dict={}):
        """
        #确认搭乘
        :param param_dict: 
        :type header_dict: key;userId
        :return:
        """
        return self.request("POST", DiDaReq.DIDA_CONFIRM, params=param_dict, headers=header_dict)
    def dida_payment(self,param_dict={}, header_dict={}):
        """
            #支付订单
            :param param_dict: 
            :type header_dict: key;userId
            :return:
        """
        return self.request("POST", DiDaReq.DIDA_PAYMENT, params=param_dict, headers=header_dict)
    def dida_price(self,param_dict={},header_dict={}):
        """
            #估价
            :param param_dict: 
            :type header_dict: key;userId
            :return:
        """
        header_dict['User-Agent'] = 'Mobike/6.6.0 (iPhone; iOS 11.1.2; Scale/2.00)'
        return self.request("POST", DiDaReq.DIDA_PRICE, params=param_dict,headers=header_dict)
    def dida_thanksfee(self, param_dict={},header_dict={}):
        '''
        增加感谢费
          @ApiParam("userId") @RequestParam("userId") String userId,
          @ApiParam("offset") @RequestParam("offset") int offset,
          @ApiParam("limit") @RequestParam("limit") int limit) 
        '''
        return self.request("POST", DiDaReq.DIDA_THANKSFEE, params=param_dict, headers=header_dict)