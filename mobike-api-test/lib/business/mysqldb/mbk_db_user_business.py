#!/usr/bin/python
#-*- decoding:utf-8 -*-

__author__ = "wangjieran@mobike.com"

import datetime

from lib.business.base_business import BaseBusiness
from lib.mbmanage.dbmanage.mobike_db_manage import MobikeDBAdmin

class MBKDBUserBusiness(BaseBusiness):
    def __init__(self):
        self.mobike_DB_admin = MobikeDBAdmin()

    def get_userid_with_mobile(self, mobileno=None):
        return self.mobike_DB_admin.get_userid_with_mobile(mobileno=mobileno)

