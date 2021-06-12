#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__="dingbaixia"

from lib.mbmanage.requestmanage.base_req import BaseReq


class SoftlockReq(BaseReq):

    #锁注册
    REGISTER_SOFTLOCK = 'lock/registry'
    #生成二维码
    QR_SOFTLOCK = 'lockQr'
    #关锁上报
    LOCK_SOFTLOCK = 'lock/lock'
    # 软锁重置
    RESET_SOFTLOCK = 'lock/reset'
    # 上报位置
    REPORT_SOFTLOCKPOSTION = 'report/position'
    #开锁确认(短信代理)
    OPEN_SOFTLOCK_SMSPROXY = 'lock/smsProxy'
    #查询用户持有的所有锁
    USER_LOCKS = 'user/locks'
    #注销锁
    DELETE = "/lock/delete"
    # 上报电池状态
    ELECTRICITY = "/report/electricity"

    def __init__(self):
        #self.host = "http://softlock.mobike.io"
        self.host = "http://10.0.70.49:8084"

    def electricity_req(self, param_dict={}):
        '''
        上报电池状态
        * @param int reason 上报类型:1 表示安装电池 2表示拔出电池 3表示例行上报 4 表示关锁电池上报
        * @param int soc 剩余电量 取值：0-100
        * @param int soh 健康状况 取值0-100
        * @param int temp 电池温度
        * @param String batId 电池ID 16位
        * @param int wsStat 开关状态 1表示开，2表示关
        * @param int batStat 电池状态 1表示有大电池，2表示无大电池
        :return:
        '''
        return self.request("GET", SoftlockReq.ELECTRICITY, param_dict)

    def register_softlock(self, param_dict={}):
        '''
        注册软锁
        :param param_dict: host
        :return: {
            code: 0,
            message: "注册成功",
            data: [
            {
            bikeId: "6516806928"
            ....}
        '''

        return self.request("GET", SoftlockReq.REGISTER_SOFTLOCK, params=param_dict)

    def lock_delte(self, param_dict={}):
        '''
        注销锁
        :param param_dict:
        :return:
        '''
        return self.request("GET", SoftlockReq.DELETE, params=param_dict)

    def reset_softlock(self, param_dict={}):
        '''
        重置锁
        :param param_dict: {userId:, bikeId:}
        :return:{ code: 0,
            message: "锁重置成功",
              data: null
            }
        '''
        return self.request("GET", SoftlockReq.RESET_SOFTLOCK, params=param_dict)

    def lock(self, param_dict={}):
        '''
        关锁
        :param param_dict:{userId:, bikeId:}
        :return:{
            "code": 0,
            "data": null,
            "message": "success"
            }
        '''
        return self.request("GET", SoftlockReq.LOCK_SOFTLOCK, params=param_dict)

    def qr(self, param_dict={}):
        '''
        生成锁的二维码
        :param param_dict: bikeId
        :return:
        '''
        return self.request("GET", SoftlockReq.QR_SOFTLOCK, params=param_dict)

    def report_softlock_position(self, param_dict={}):
        '''
        上报位置
        :param param_dict: bikeId, userId
        :return:{
            "code": 0,
            "data": null,
            "message": "success"
            }
        '''
        return self.request("GET", SoftlockReq.REPORT_SOFTLOCKPOSTION, params=param_dict)

    def open_softlock_with_smsproxy(self, param_dict={}):
        '''
        开锁确认(短信代理)
        :param param_dict:imsi, mobile, content
        :return:{
            "code": 0,
            "data": null,
            "message": "success"
            }
        '''
        return self.request("GET", SoftlockReq.OPEN_SOFTLOCK_SMSPROXY, params=param_dict)

    def get_user_alllocks(self, param_dict={}):
        '''
        查询用户持有的所有锁
        :param param_dict:userId
        :return:
        '''
        return self.request("GET", SoftlockReq.USER_LOCKS, params=param_dict)