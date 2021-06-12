#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'
import json
from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class CouponUser(BaseReq):

    def __init__(self):
        super(CouponUser, self).__init__(micro_service_name=MicroServiceName.PANDORA_COUPON)

    # 获取用户名下优惠券列表
    GET_COUPON_LIST = "couponUser/getAvailableCouponDetailsList"

    # 活动发券
    # OFFER_ACTIVITY= "couponUser/offerActivity"
    OFFER_ACTIVITY = "coupon/receivebyactivity"

    # 根据ID获取优惠券
    GET_DETAIL_BY_ID = "couponUser/getUserCouponDetailsById"

    # 锁券
    LOCK = "couponUser/lockCoupon"

    # 用券
    USE = "couponUser/useCoupon"

    # 解锁
    UNLOCK = "couponUser/unlockCoupon"

    # 退券
    RETURN_COUPON = "couponUser/returnCoupon"

    def lock_coupon_req(self, param={}, header={}):
        #header['Content-Type'] = "application/json"
        return self.request("POST", CouponUser.LOCK, params=param, headers=header)

    def use_coupon_req(self, param={}, header={}):
        return self.request("POST", CouponUser.USE, params=param, headers=header)

    def unlock_coupon_req(self, param={}, header={}):
        return self.request("POST", CouponUser.UNLOCK, params=param, headers=header)

    def return_coupon_req(self, param={}, header={}):
        return self.request("POST", CouponUser.RETURN_COUPON, params=param, headers=header)



    def get_coupon_list_req(self, param={}, header={}):
        '''获取用户名下优惠券列表'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponUser.GET_COUPON_LIST, params=json.dumps(param), headers=header)

    def offer_activity_req(self, param={}, header={}):
        '''活动发券'''
        header['Content-Type'] = "application/json"
        return self.request("POST", CouponUser.OFFER_ACTIVITY, params=json.dumps(param), headers=header)

    def get_detail_by_id_req(self, param={}, header={}):
        ''''''
        #header['Content-Type'] = "application/json"
        return self.request("POST", CouponUser.GET_DETAIL_BY_ID, params=param, headers=header)

