#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq


class ActivityGigtReq(BaseReq):
    '''
    合作方发优惠券
    '''
    def __init__(self):
        super(ActivityGigtReq, self).__init__()

    # 发券合作方管理通过id获得某条详情信息的接口
    GET_SUPPLIER = "athena/activity/giftshare/getonesupplier.do"
    # 发券合作方管理编辑接口
    EDIT_SUPPLIER = "athena/activity/giftshare/editsupplier.do"
    # 发券合作方新建接口
    CREATE_SUPPLIER = "athena/activity/giftshare/createsupplier.do"

    DELETE_SUPPLER = 'athena/activity/giftshare/deletesupplier.do'
    # 发券合作方管理列表页
    SUPPLIER_LIST = "athena/activity/giftshare/supplierlist.do"
    # 请求摩拜优惠券接口
    COUPON_INFO = "athena/coupon/info/queryCouponInfo.do"
    # H5页接口请求活动信息
    GET_ONE_ACTIVITY = 'api/activity/activity/giftshare/getoneactivity.do'
    # 生成福袋接口
    RECORD = 'api/v2/clock-in/record.do'
    # 根据打卡记录计算并查看福袋详情接口
    PACKET_DETAIL = 'api/v2/clock-in/packetDetail.do'
    # 确认分享接口
    FINISH_SHARE = 'api/v2/clock-in/finishShare.do'
    # 兑换接口
    APPLY = 'api/v2/activity/giftshare/apply.do'
    # 合作方优惠券H5列表页接口
    ACTIVITY_LIST= "athena/activity/giftshare/activitylist.do"
    # 合作方优惠券H5新建接口
    CREATE_ACTIVITY = "athena/activity/giftshare/createactivity.do"
    # 合作方优惠券H5编辑接口
    EDIT_ACTIVITY = "athena/activity/giftshare/editactivity.do"
    # 请求活动的详情接口
    ATHENA_GET_ONE_ACTIVITY = "athena/activity/giftshare/getoneactivity.do"

    DELETE_EVENT = "athena/activity/giftshare/batchdeleteevent.do"

    def delete_event(self, param):
        return self.request("POST", ActivityGigtReq.DELETE_EVENT, param)

    def delete_supplier(self, param):
        return self.request("POST", ActivityGigtReq.DELETE_SUPPLER, params=param)

    def get_supplier(self, param):
        return self.request("GET", ActivityGigtReq.GET_SUPPLIER, params=param)

    def edit_supplier(self, param):
        return self.request("POST", ActivityGigtReq.EDIT_SUPPLIER, params=param)

    def create_supplier(self, param):
        return self.request("POST", ActivityGigtReq.CREATE_SUPPLIER, params=param)

    def supplier_list(self, param):
        return self.request("GET", ActivityGigtReq.SUPPLIER_LIST, params=param)

    def coupon_info(self):
        return self.request("POST", ActivityGigtReq.COUPON_INFO,)

    def athena_get_one_activity(self, param):
        return self.request("GET", ActivityGigtReq.ATHENA_GET_ONE_ACTIVITY, params=param)

    def edit_activity(self, param):
        return self.request("POST", ActivityGigtReq.EDIT_ACTIVITY, params=param)

    def create_activity(self, param):
        return self.request("POST", ActivityGigtReq.CREATE_ACTIVITY, params=param)

    def activity_list(self, param_dict={}):
        return self.request("GET", ActivityGigtReq.ACTIVITY_LIST, params=param_dict)

    def get_one_activity(self, param_dict={}):
        '''
        请求活动信息
        :param param_dict:id：
        :return:
        '''
        return self.request("GET", ActivityGigtReq.GET_ONE_ACTIVITY, params=param_dict)

    def apply(self, param_dict={}):
        '''
        兑换接口
        :param param_dict:mobile, id
        :return:
        '''
        return self.request("GET", ActivityGigtReq.APPLY, params=param_dict)

    def record(self, header_dict=None, param_dict=None):
        '''
        生成福袋
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", ActivityGigtReq.RECORD, params=param_dict, headers=header_dict)

    def packet_detail(self, header_dict=None, param_dict=None):
        '''
        查看福袋详情
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", ActivityGigtReq.PACKET_DETAIL, params=param_dict, headers=header_dict)

    def finish_share(self, header_dict=None, param_dict=None):
        '''
        确认分享
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", ActivityGigtReq.FINISH_SHARE, params=param_dict, headers=header_dict)