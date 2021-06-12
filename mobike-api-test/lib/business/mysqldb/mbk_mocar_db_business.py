#!/usr/bin/python
#-*- decoding:utf-8 -*-
import json

from lib.entity.db_entity.mbk_mocar import MBKCarUser
from lib.mbmanage.dbmanage.mbk_mocar_admin import MBKCarUserTable, MBKCarBookingTable, MBKCarOrderTable, \
    MBKCarPeccancyRecordTable, MBKCarDepositRecordTable, MBKCarTypeInfoTable, MBKCarUserDepositCouponTable
from lib.util.time_util import TimeUtil

__author__ = "yuanyongsheng@mobike.com"


class MBKMocarUserDBBusiness(object):
    def __init__(self):
        self.mbk_trialrecords = MBKCarUserTable()

    def update(self, where_instance, update_instance):
        self.mbk_trialrecords.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_trialrecords.add_record(instance)

    def delete(self, where_instance):
        self.mbk_trialrecords.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_trialrecords.select(where_instance,*args)

class MBKMocarBookingDBBusiness(object):
    def __init__(self):
        self.mbk_carbooking = MBKCarBookingTable()

    def update(self, where_instance, update_instance):
        self.mbk_carbooking.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_carbooking.add_record(instance)

    def delete(self, where_instance):
        self.mbk_carbooking.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_carbooking.select(where_instance,*args)

class MBKMocarOrderDBBusiness(object):
    def __init__(self):
        self.mbk_carorder = MBKCarOrderTable()

    def update(self, where_instance, update_instance):
        self.mbk_carorder.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_carorder.add_record(instance)

    def delete(self, where_instance):
        self.mbk_carorder.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_carorder.select(where_instance,*args)

class MBKCarPeccancyRecordTDBBusiness(object):
    def __init__(self):
        self.mbk_carPeccancy = MBKCarPeccancyRecordTable()

    def update(self, where_instance, update_instance):
        self.mbk_carPeccancy.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_carPeccancy.add_record(instance)

    def delete(self, where_instance):
        self.mbk_carPeccancy.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_carPeccancy.select(where_instance,*args)

class MBKCarDepositRecordTDBBusiness(object):
    def __init__(self):
        self.mbk_car_deposit = MBKCarDepositRecordTable()

    def update(self, where_instance, update_instance):
        self.mbk_car_deposit.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_car_deposit.add_record(instance)

    def delete(self, where_instance):
        self.mbk_car_deposit.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_car_deposit.select(where_instance,*args)

class MBKCarTypeInfoDBBusiness(object):
    def __init__(self):
        self.mbk_car_type_info = MBKCarTypeInfoTable()

    def update(self, where_instance, update_instance):
        self.mbk_car_type_info.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_car_type_info.add_record(instance)

    def delete(self, where_instance):
        self.mbk_car_type_info.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_car_type_info.select(where_instance,*args)

class MBKCarUserDepositCouponDBBusiness(object):
    def __init__(self):
        self.mbk_car_deposit_coupon = MBKCarUserDepositCouponTable()

    def update(self, where_instance, update_instance):
        self.mbk_car_deposit_coupon.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_car_deposit_coupon.add_record(instance)

    def delete(self, where_instance):
        self.mbk_car_deposit_coupon.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_car_deposit_coupon.select(where_instance,*args)



if __name__ == "__main__":
    a= MBKMocarUserDBBusiness()
    instance = MBKCarUser()
    instance.start_time = "2017-11-24 16:52:37"
    instance.user_id = "dfasfdsafdsg"
    instance.end_time = TimeUtil.format_timer_to_str()
    instance.country_code =1
    instance.notified =  0
    instance.paid_deposit = 0
    #a.save(instance)
    where_instance = MBKCarUser()
    where_instance.user_id = instance.user_id

    a.update(where_instance=where_instance, update_instance=instance)