#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class ModouV2Req(BaseReq):
    def __init__(self):
        super(ModouV2Req, self).__init__(micro_service_name=MicroServiceName.MODOUV2)

    def modouv2_getmocoinlist(self, param_dict=None):
        '''
        积分明细，分页
        '''
        return self.request("GET", "modouv2/getMoCoinList", params=param_dict)

    def modouv2_insertridebonusmocoin(self, param_dict=None):
        '''
        停车有奖发积分，有订单id，分数，type（加分不超过配置上线）
        '''
        return self.request("POST", "modouv2/insertRideBonusMoCoin", params=param_dict)

    def modouv2_getmocoinbyorder(self, param_dict=None):
        '''
        根据用户id和订单id，查询积分明细
        '''
        return self.request("GET", "modouv2/getMoCoinByOrder", params=param_dict)

    def modouv2_receivemocoinlastweek(self, param_dict=None):
        '''
        领取最近一周内积分，加总分
        '''
        return self.request("POST", "modouv2/receiveMoCoinLastWeek", params=param_dict)

    def modouv2_insertfeedbackmocoinlist(self, param_dict=None):
        '''
        报障有效 批量添加积分
        '''
        return self.request("POST", "modouv2/insertFeedbackMoCoinList", params=param_dict)

    def modouv2_insertprizemocoin(self, param_dict=None):
        '''
        活动/分享/报障添加积分明细（修改总分）
        类型，4：分享获得 5：报障获得
        描述，传stringtable key，分享：MOCOIN_TYPE_SHARE 报障：MOCOIN_TYPE_WRONG_PARK
        '''
        return self.request("POST", "modouv2/insertPrizeMoCoin", params=param_dict)

    def modouv2_syncmodouprizemodel(self, param_dict=None):
        '''
        同步兑吧商品
        '''
        return self.request("POST", "modouv2/syncModouPrizeModel", params=param_dict)

    def modouv2_inittotalmocoin(self, param_dict=None):
        '''
        初始化总分(1 老积分总分转换 + 新分明细 2 无老积分总分 + 新分明细； 新增初始化明细，新增总分
        '''
        return self.request("POST", "modouv2/initTotalMoCoin", params=param_dict)

    def modouv2_updateexchangeresult(self, param_dict=None):
        '''
        兑换结果修改
        '''
        return self.request("POST", "modouv2/updateExchangeResult", params=param_dict)

    def modouv2_exchangeprize(self, param_dict=None):
        '''
        兑换商品
        '''
        return self.request("POST", "modouv2/exchangePrize", params=param_dict)

    def modouv2_batchupdatemocoingetstatus(self, param_dict=None):
        '''
        批量更新明细表（结费页领取积分）
        '''
        return self.request("POST", "modouv2/batchUpdateMoCoinGetStatus", params=param_dict)

    def modouv2_insertridemocoin(self, param_dict=None):
        '''
        骑行基础发积分，添加积分明细（不修改总分）
        '''
        return self.request("POST", "modouv2/insertRideMoCoin", params=param_dict)

    def modouv2_setwrongparkredpoint(self, param_dict=None):
        '''
        设置报障红点，存缓存
        '''
        return self.request("POST", "modouv2/setWrongParkRedpoint", params=param_dict)

    def modouv2_cancelmocoin(self, param_dict=None):
        '''
        兑换失败撤销魔豆: 恢复总魔豆数目，删除魔豆记录
        '''
        return self.request("POST", "modouv2/cancelMoCoin", params=param_dict)

    def modouv2_getrideredpoint(self, param_dict=None):
        '''
        获取骑行红点是否有 0无 1有
        '''
        return self.request("GET", "modouv2/getRideRedpoint", params=param_dict)

    def modouv2_getwrongparkredpoint(self, param_dict=None):
        '''
        获取报障红点是否有 0无 1有
        '''
        return self.request("GET", "modouv2/getWrongParkRedpoint", params=param_dict)

    def modouv2_syncmodouprizeids(self, param_dict=None):
        '''
        同步兑吧商品，特定商品id
        '''
        return self.request("POST", "modouv2/syncModouPrizeIds", params=param_dict)

    def modouv2_getmocoinlistforathena(self, param_dict=None):
        '''
        积分明细，分页，雅典娜使用
        '''
        return self.request("GET", "modouv2/getMoCoinListForAthena", params=param_dict)

    def modouv2_gettotalmocoins(self, param_dict=None):
        '''
        查询用户总分
        '''
        return self.request("GET", "modouv2/getTotalMoCoins", params=param_dict)

    def modouv2_receivemocoinbyorder(self, param_dict=None):
        '''
        领取订单魔币
        '''
        return self.request("POST", "modouv2/receiveMoCoinByOrder", params=param_dict)

    def modouv2_returnmocoin(self, param_dict=None):
        '''
        退还积分（修改明细状态exchange_status，新增明细记录type=退还）
        '''
        return self.request("POST", "modouv2/returnMoCoin", params=param_dict)

    def modouv2_getridemocoinsbytype(self, param_dict=None):
        '''
        根据类型获取积分记录
        '''
        return self.request("GET", "modouv2/getRideMocoinsByType", params=param_dict)

    def modouv2_querymocoinlastweek(self, param_dict=None):
        '''
        查询最近一周内未领取积分
        '''
        return self.request("GET", "modouv2/queryMoCoinLastWeek", params=param_dict)

    def modouv2_setrideredpoint(self, param_dict=None):
        '''
        设置骑行红点
        '''
        return self.request("POST", "modouv2/setRideRedpoint", params=param_dict)

