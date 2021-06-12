#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName


class GeoFencingReq(BaseReq):

    def __init__(self):
        super(GeoFencingReq, self).__init__(micro_service_name=MicroServiceName.GEO_FENCINF)

    def initIndex(self):
        '''删除电子围栏后需要清楚缓存才能生效'''
        return self.request("POST", "/geofencing/initIndex?")