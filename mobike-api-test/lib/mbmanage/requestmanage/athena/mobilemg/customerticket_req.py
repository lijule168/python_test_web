#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class CustomerTicketReq(BaseReq):

    def __init__(self):
        super(CustomerTicketReq, self).__init__()

    def customerticket_item(self, json_data=None):
        '''
        客服回复反馈
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", "athena/mobilemg/ticket/item.do", json_data=json_data, headers=header_dict)


