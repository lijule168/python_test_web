#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'
import json
from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName


class CouponTemplateReq(BaseReq):
    def __init__(self):
        super(CouponTemplateReq, self).__init__(micro_service_name=MicroServiceName.PANDORA_COUPON)

    ADD_TEMPLATE= '/coupon/addCouponTemplate'
    GET_TEMPLATE_LIST = "/coupon/getCouponTemplateList"
    DELTE_TEMPLATE = "/coupon/deleteCouponTemplate"

    def add_coupon_template(self, param={}, header={}):
        '''添加模版'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponTemplateReq.ADD_TEMPLATE, params=json.dumps(param), headers=header)

    def get_template_list(self, param={}, header={}):
        '''获取活动列表'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponTemplateReq.GET_TEMPLATE_LIST, params=json.dumps(param), headers=header)

    def delete_template_req(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponTemplateReq.DELTE_TEMPLATE, params=json.dumps(param), headers=header)

