#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class I18nReq(BaseReq):
    #国际化获取用户基本状态
    GET_I18NSTATEINFOS = "api/v2/i18n/state"

    def __init__(self):
        super(I18nReq, self).__init__()

    def geti18nStateInfos(self, header_dict={}):
        '''
        国际化获取用户基本状态
        :param header_dict
        :return:
        '''
        return self.request("GET", self.__class__.GET_I18NSTATEINFOS, headers=header_dict)

    def geti18nStateInfos(self, header_dict={}):
        '''
        国际化获取用户基本状态
        :param header_dict
        :return:
        '''
        return self.request("GET", self.__class__.GET_I18NSTATEINFOS, headers=header_dict)