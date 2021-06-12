#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'
import json
from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class CouponActivityReq(BaseReq):
    def __init__(self):
        super(CouponActivityReq, self).__init__(micro_service_name=MicroServiceName.PANDORA_COUPON)

    # 添加活动
    ADD_COUPON_ACTIVITY = "couponActivity/addCouponActivity"

    # 活动列表
    GET_COUPON_ACTIVITY_LIST = "couponActivity/getCouponActivityList"

    UPDATE_COUPON_STATUS= "couponActivity/updateCouponActivityStatus"

    BIND_COUPON_TASK = "couponActivity/bindCouponTasks"

    DELTE_ACTIVITY = "couponActivity/deleteCouponActivity"

    def delte_acstivity_req(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponActivityReq.DELTE_ACTIVITY, params=json.dumps(param), headers=header)


    def add_coupon_activity(self, param={}, header={}):
        '''添加活动'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponActivityReq.ADD_COUPON_ACTIVITY, params=json.dumps(param), headers=header)

    def get_coupon_activity_list(self, param={}, header={}):
        '''活动列表'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponActivityReq.GET_COUPON_ACTIVITY_LIST, params=json.dumps(param), headers=header)

    def update_coupon_activity_status(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponActivityReq.UPDATE_COUPON_STATUS, params=json.dumps(param), headers=header)

    def bind_coupon_task(self, param={}, header={}):
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponActivityReq.BIND_COUPON_TASK, params=json.dumps(param), headers=header)