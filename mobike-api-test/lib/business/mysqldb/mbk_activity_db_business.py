#!/usr/bin/python
#-*- decoding:utf-8 -*-
import json

from lib.util.time_util import TimeUtil

__author__ = "dingbaixia@mobike.com"

from lib.mbmanage.dbmanage.mbk_activity_admin import MBKTrailRecordsTable
from lib.entity.db_entity.mbk_activity import MBK_Tial_Records

class MBKTrailRecordsTBBusiness(object):
    def __init__(self):
        self.mbk_trialrecords = MBKTrailRecordsTable()

    def update(self, where_instance, update_instance):
        self.mbk_trialrecords.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_trialrecords.add_record(instance)

    def delete(self, where_instance):
        self.mbk_trialrecords.del_record(where_instance)

if __name__ == "__main__":
    a= MBKTrailRecordsTBBusiness()
    instance = MBK_Tial_Records()
    instance.start_time = "2017-11-24 16:52:37"
    instance.user_id = "dfasfdsafdsg"
    instance.end_time = TimeUtil.format_timer_to_str()
    instance.country_code =1
    instance.notified =  0
    instance.paid_deposit = 0

    #a.save(instance)
    where_instance = MBK_Tial_Records()
    where_instance.user_id = instance.user_id

    a.update(where_instance=where_instance, update_instance=instance)