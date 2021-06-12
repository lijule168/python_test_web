#!/usr/bin/python
# -*- coding:utf-8 -*-
import json

__author__='dingbaixia'

from lib.mbmanage.dbmanage.db_model.mbk_activity_model import _MBKClockInConfigModel, _MBKClockInModel, _MBKGiftShareEvent, _MBKGiftShareSupplier, _MBKTrialRecordsModel
from lib.entity.db_entity.mbk_activity import MBK_Tial_Records


class MBKActivityDBAdmin(object):
    def __init__(self):
        pass

    def add_clockin_record(self, user_id, bonus, bonus_withdraw, clock_in_days, create_time, last_clock_in, last_withdraw):
        '''
        添加打卡记录
        :param user_id:
        :param bonus:
        :param bonus_withdraw:
        :param clock_in_days:
        :param create_time:
        :param last_clock_in:
        :param last_withdraw:
        :return:
        '''
        mbk_clockin = _MBKClockInModel()
        mbk_clockin.insert(user_id=user_id, bonus=bonus, bonus_withdraw=bonus_withdraw, clock_in_days=clock_in_days,
                           create_time=create_time, last_clock_in=last_clock_in, last_withdraw=last_withdraw)

    def add_supplier(self, name, requesturl, createtime, updatetime, appkey, source, logo):
        mbk_supplier = _MBKGiftShareSupplier()
        mbk_supplier.insert(name=name, requesturl=requesturl, createtime=createtime, updatetime=updatetime,
                            appkey=appkey, source=source, logo=logo)

    def add_gift_share_event(self, title, imgurl, imgjumplink, createtime, updatetime, ison, sharingtitle, shareingsubtitle,
                            shareingimgurl, comments, mobikegifts, mobikeexchangecode, outsidegifts):
        '''
        添加合作方活动信息
        :param title:
        :param imgurl:
        :param imgjumplink:
        :param createtime:
        :param updatetime:
        :param ison:
        :param sharingtitle:
        :param shareingsubtitle:
        :param shareingimgurl:
        :param comments:
        :param mobikegifts:
        :param mobikeexchangecode:
        :param outsidegifts:
        :return:
        '''
        mbk_gift_event = _MBKGiftShareEvent()
        mbk_gift_event.insert(title=title, imgurl=imgurl, imgjumplink=imgjumplink, createtime=createtime,
                              updatetime=updatetime, ison=ison, sharingtitle=sharingtitle, shareingsubtitle=shareingsubtitle,
                              shareingimgurl=shareingimgurl, comments=comments, mobikegifts=mobikegifts,
                              mobikeexchangecode=mobikeexchangecode, outsidegifts=outsidegifts)

    def del_clockin_record_by_userid(self, user_id):
        '''

        :param user_id:
        :return:
        '''
        mbk_clockin = _MBKClockInModel()
        mbk_clockin.where(user_id=user_id).delete()

    def update_clockin_config(self, name, value):
        '''
        更新配置信息
        :param name:
        :param value:
        :return:
        '''
        mbkclockin_config = _MBKClockInConfigModel()
        mbkclockin_config.where(name=name).update(value=value)

    def select_supplier_id(self, createtime):
        supplier = _MBKGiftShareSupplier()
        return supplier.where(createtime=createtime).select('supplierId')

class MBKTrailRecordsTable(object):

    def select(self, *args):
        instance = _MBKTrialRecordsModel()
        records = instance.select(*args)
        return records

    def add_record(self, instance):
        instance = _MBKTrialRecordsModel(**instance.__dict__)
        instance.save()

    def update_record(self, where_instance, update_instance):

        instance = _MBKTrialRecordsModel()
        if where_instance is None:
            instance.update(**update_instance.__dict__)
        else:
            instance.where(**where_instance.__dict__).update(**update_instance.__dict__)

    def del_record(self, where_instance):
        instance = _MBKTrialRecordsModel()
        if where_instance is None:
            instance.delete()
        else:
            instance.where(**where_instance.__dict__).delete()