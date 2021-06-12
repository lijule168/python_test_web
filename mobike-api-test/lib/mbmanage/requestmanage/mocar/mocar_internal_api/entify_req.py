#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class EntifyReq(BaseReq):
    def __init__(self):
        super(EntifyReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_INTERNAL_API)

    def addcar2parking(self, param_dict=None):
        '''
        将车辆移入指定停车场
        '''
        return self.request("POST", "entity/car/addCar2Parking.do", params=param_dict)

    def addcarlist(self, param_dict=None):
        '''
        批量新增车辆信息
        '''
        return self.request("POST", "entity/car/addCarList.do", params=param_dict)

    def remove(self, param_dict=None):
        '''
        删除停车场
        '''
        return self.request("POST", "entity/parking/remove.do", params=param_dict)

    def updaterecord(self, param_dict=None):
        '''
        更新车辆故障记录
        '''
        return self.request("POST", "entity/fault/updateRecord.do", params=param_dict)

    def addcar(self, json_dict=None):
        '''
        新增车辆信息
        '''
        return self.request("POST", "entity/car/addCar.do", json_data=json_dict)

    def editcarinfo(self, param_dict=None):
        '''
        编辑车辆信息
        '''
        return self.request("POST", "entity/car/editCarInfo.do", params=param_dict)

    def searchparking(self, param_dict=None):
        '''
        *通过关键词搜索停车场
        '''
        return self.request("GET", "entity/parking/searchParking.do", params=param_dict)

    def record(self, json_dict=None):
        '''
        登记车辆故障
        '''
        return self.request("POST", "entity/fault/record.do", json_data=json_dict)

    def add(self, param_dict=None):
        '''
        添加停车场
        '''
        return self.request("POST", "entity/parking/add.do", params=param_dict)

    def edit(self, param_dict=None):
        '''
        编辑停车场
        '''
        return self.request("POST", "entity/parking/edit.do", params=param_dict)

    def distance(self, param_dict=None):
        '''
        *获取车辆与指定停车场的距离
        '''
        return self.request("GET", "entity/parking/distance.do", params=param_dict)

    def uploadtypeimage(self, param_dict=None):
        '''
        上传车型图片
        '''
        return self.request("POST", "entity/carType/uploadTypeImage.do", params=param_dict)

    def addcartype(self, json_dict=None):
        '''
        新增车辆类型
        '''
        return self.request("POST", "entity/carType/addCarType.do", json_data=json_dict)

    def getcarinfo(self, param_dict=None):
        '''
        查看车辆信息
        '''
        return self.request("GET", "entity/car/getCarInfo.do", params=param_dict)

    def editcartype(self, json_dict=None):
        '''
        编辑车辆类型
        '''
        return self.request("POST", "entity/carType/editCarType.do", json_data=json_dict)

    def gettype(self, param_dict=None):
        '''
        通过id查看车辆类型
        '''
        return self.request("GET", "entity/carType/getType.do", params=param_dict)

    def list(self, param_dict=None):
        '''
        查看车辆报障记录
        '''
        return self.request("GET", "entity/fault/list.do", params=param_dict)

    def getparking(self, param_dict=None):
        '''
        *查看当前城市停车场
        '''
        return self.request("GET", "entity/parking/getParking.do", params=param_dict)

    def removecar(self, param_dict=None):
        '''
        移除车辆信息
        '''
        return self.request("POST", "entity/car/removeCar.do", params=param_dict)

    def getcarinparking(self, param_dict=None):
        '''
        查找当前停车场的车辆
        '''
        return self.request("GET", "entity/car/getCarInParking.do", params=param_dict)

    def getalltype(self, param_dict=None):
        '''
        通过品牌查看车辆类型
        '''
        return self.request("GET", "entity/carType/getAllType.do", params=param_dict)

