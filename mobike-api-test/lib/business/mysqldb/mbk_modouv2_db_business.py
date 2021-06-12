#!/usr/bin/python
#-*- decoding:utf-8 -*-
import json

from lib.entity.db_entity.mbk_mocar import MBKCarUser
from lib.entity.db_entity.mbk_modou import MBKModouV2
from lib.mbmanage.dbmanage.mbk_mocar_admin import MBKCarUserTable, MBKCarBookingTable, MBKCarOrderTable, \
    MBKCarPeccancyRecordTable, MBKCarDepositRecordTable, MBKCarTypeInfoTable, MBKCarUserDepositCouponTable
from lib.mbmanage.dbmanage.mbk_modou_admin import MBKModouV2Table, MBKModouTotalV2Table
from lib.util.time_util import TimeUtil

__author__ = "yuanyongsheng@mobike.com"


class MBKModouV2DBBusiness(object):
    def __init__(self):
        self.mbk_modouv2 = MBKModouV2Table()

    def update(self, where_instance, update_instance):
        self.mbk_modouv2.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_modouv2.add_record(instance)

    def delete(self, where_instance):
        self.mbk_modouv2.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_modouv2.select(where_instance,*args)

class MBKModouTotalV2DBBusiness(object):
    def __init__(self):
        self.mbk_modoutotalv2 = MBKModouTotalV2Table()

    def update(self, where_instance, update_instance):
        self.mbk_modoutotalv2.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_modoutotalv2.add_record(instance)

    def delete(self, where_instance):
        self.mbk_modoutotalv2.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_modoutotalv2.select(where_instance,*args)


if __name__ == "__main__":
    a= MBKModouV2DBBusiness()
    instance = MBKModouV2()
    instance.start_time = "2017-11-24 16:52:37"
    instance.user_id = "dfasfdsafdsg"
    instance.end_time = TimeUtil.format_timer_to_str()
    instance.country_code =1
    instance.notified =  0
    instance.paid_deposit = 0
    #a.save(instance)
    where_instance = MBKModouV2()
    where_instance.user_id = instance.user_id

    a.update(where_instance=where_instance, update_instance=instance)