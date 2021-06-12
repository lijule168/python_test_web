#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class Iafc(BaseReq):
    def __init__(self):
        super(Iafc, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def iafc_createAccount(self, param_dict=None, header_dict=None):
        '''
        insert user relation
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("GET", "iafc/createAccount", params=param_dict, headers=header_dict)

class TicketCodeReq(BaseReq):
    def __init__(self):
        super(TicketCodeReq, self).__init__()

    def ticket_gettickets(self, param_dict=None, header_dict=None):
        '''
        Get new QRCodes
        '''
        return self.request("GET", "api/orthrus/orthrus-basicinfo/ticket/getTickets", params=param_dict, headers=header_dict)

    def iafc_createAccount(self, param_dict=None, header_dict=None):
        '''
        insert user relation
        :param param_dict:
        :param header_dict:
        :return:
        '''
        iafc = Iafc()
        return iafc.iafc_createAccount(param_dict=param_dict, header_dict=header_dict)

    def ticket_scantickets(self, param_dict=None, header_dict=None):
        '''
        scan QRcodes to get status
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/ticket/scanTickets", params=param_dict, headers=header_dict)




