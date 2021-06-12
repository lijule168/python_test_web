#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class FreeDepositReq(BaseReq):
    def __init__(self):
        super(FreeDepositReq, self).__init__()

    def applyfreedeposit(self , param_dict=None, header_dict=None):
        '''
        申请腾讯征信免押金
        '''
        return self.request("POST", "api/v2/freeDeposit/applyFreeDeposit.do", params=param_dict, headers=header_dict)

