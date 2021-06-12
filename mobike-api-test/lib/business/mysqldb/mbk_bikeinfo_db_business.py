#!/usr/bin/python
#-*- decoding:utf-8 -*-
import json

from lib.entity.db_entity.mbk_mocar import MBKCarUser
from lib.mbmanage.dbmanage.mbk_bikeinfo_admin import MBKImsiMobikeTable, MBKBikeHardwareTable
from lib.util.time_util import TimeUtil

__author__ = "yuanyongsheng@mobike.com"


class MBKImsiMobikeDBBusiness(object):
    def __init__(self):
        self.mbk_imsimobike= MBKImsiMobikeTable()

    def update(self, where_instance, update_instance):
        self.mbk_imsimobike.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_imsimobike.add_record(instance)

    def delete(self, where_instance):
        self.mbk_imsimobike.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_imsimobike.select(where_instance,*args)

class MBKBikeHardwareDBBusiness(object):
    def __init__(self):
        self.mbk_bikehardware = MBKBikeHardwareTable()

    def update(self, where_instance, update_instance):
        self.mbk_bikehardware.update_record(update_instance=update_instance, where_instance=where_instance)

    def save(self, instance):
        self.mbk_bikehardware.add_record(instance)

    def delete(self, where_instance):
        self.mbk_bikehardware.del_record(where_instance)

    def selete(self,where_instance,*args):
        return self.mbk_bikehardware.select(where_instance,*args)


