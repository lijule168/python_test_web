#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "dingbaixia"

import copy
from lib.common.config_helper import EnvConfig

class BaseDBAdmin(object):
    def __init__(self, db_name="mbk_db"):
        self.conn_obj = copy.deepcopy(EnvConfig().mobkie_db_conn_params)
        self.conn_obj.db_name = db_name
