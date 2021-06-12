#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.common.orm.model import Model
from lib.common.orm.field import *
from lib.mbmanage.dbmanage.base_db_manage import BaseDBAdmin

class _MBKTrialRecordsModel(Model):
    __table__ = "mbk_trial_records"
    __db_conn__ = BaseDBAdmin(db_name="mbk_activity").conn_obj
    id = IntegerField(name="id", primary_key=True, comment='''主键''')
    user_id = StringField(name="user_id", column_type='varchar(35)', comment='''用户编码''')
    country_code = StringField(name="country_code", column_type='varchar(32)', comment='''用户请求国家''')
    city_code = StringField(name="city_code", column_type='varchar(32)', comment='''用户请求城市''')
    start_time = DateTimeField(name="start_time", comment='''开始时间''')
    end_time = DateTimeField(name="end_time", comment='''结束时间''')
    notified = IntegerField(name="notified", comment='''是否被通知''')
    paid_deposit = IntegerField(name="paid_deposit", comment='''是否已经交押金''')
    creator = StringField(name="creator", column_type='varchar(50)', comment='''创建者''')
    create_time = TimestampField(name="create_time", comment='''创建时间''')
    updator = StringField(name="updator", column_type='varchar(50)', comment='''修改者''')
    update_time = TimestampField(name="update_time", comment='''修改时间''')
    version = IntegerField(name="version", comment='''版本''')

