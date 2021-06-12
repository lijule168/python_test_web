#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq


class DriverWalletReq(BaseReq):
    def __init__(self):
        super(DriverWalletReq, self).__init__()

    def wallet_money(self, param_dict=None, header_dict=None):
        '''
        司机钱包余额查询
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("GET", "api/chariot-nfs/wallet/money", params=param_dict, headers=header_dict)


    def wallet_detail(self, param_dict=None, header_dict=None):
        '''
        查询司机钱包
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("GET", "api/chariot-nfs/wallet/details", params=param_dict, headers=header_dict)

    def with_draw(self, param_dict=None, header_dict=None):
        '''
        提现
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/chariot-nfs/wallet/withdraw", params=param_dict, headers=header_dict)