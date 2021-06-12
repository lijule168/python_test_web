#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CustomerTicketReq(BaseReq):
    def __init__(self):
        super(CustomerTicketReq, self).__init__()

    def ticket_additem(self, param_dict=None, header_dict=None):
        '''
        获取用户中心消息列表
        '''
        return self.request("POST", "api/v2/ticket/addItem.do", params=param_dict, headers=header_dict)

    def ticket_detail(self, param_dict=None, header_dict=None):
        '''
        获取用户上报详细交互内容
        '''
        return self.request("POST", "api/v2/ticket/detail.do", params=param_dict, headers=header_dict)

    def ticket_list(self, param_dict=None, header_dict=None):
        '''
        获取用户上报消息列表
        '''
        return self.request("POST", "api/v2/ticket/list.do", params=param_dict, headers=header_dict)

