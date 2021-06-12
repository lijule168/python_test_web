#!/usr/bin/python
#-*- decoding:utf-8 -*-
import json

from lib.entity.db_entity.mbk_mocar import MBKCarUser
from lib.mbmanage.dbmanage.mbk_bike_admin import MBKBikeInfoDBAdmin
from lib.util.time_util import TimeUtil

__author__ = "zhangjiangtao@mobike.com"


class MBKImsiMobikeDBBusiness(object):
    def __init__(self):
        self.mbk_bike= MBKBikeInfoDBAdmin()

    def update(self, where_instance, update_instance):
        self.mbk_bike.update_record(update_instance=update_instance, where_instance=where_instance)


