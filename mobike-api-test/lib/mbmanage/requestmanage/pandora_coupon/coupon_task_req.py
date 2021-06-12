#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'
import json
from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class CouponTaskReq(BaseReq):
    def __init__(self):
        super(CouponTaskReq, self).__init__(micro_service_name=MicroServiceName.PANDORA_COUPON)

    ADD_COUPON_TASK = "couponTask/addCouponTask"

    GET_COUPON_TASK_LIST = 'couponTask/getCouponTaskList'

    def add_coupon_task_req(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponTaskReq.ADD_COUPON_TASK, params=json.dumps(param), headers=header)

    def get_coupon_task_list(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponTaskReq.GET_COUPON_TASK_LIST, params=json.dumps(param), headers=header)