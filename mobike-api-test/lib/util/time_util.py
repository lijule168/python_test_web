#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time, datetime

class TimeUtil(object):
    @staticmethod
    def format_timer_to_str(time_stamp=None, format_date="%Y-%m-%d %H:%M:%S"):
        # if time_stamp is None:
        #     time_stamp = time.time()
        return time.strftime(format_date, time.localtime(time_stamp))

    @staticmethod
    def delta_days(days, format_date="%Y%m%d"):
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=days)
        n_days = now + delta
        return  n_days.strftime(format_date)

    @staticmethod
    def delta_seconds(seconds, format_date="%Y-%m-%d %H:%M:%S"):
        now = datetime.datetime.now()
        delta = datetime.timedelta(seconds=seconds)
        n_days = now + delta
        return  n_days.strftime(format_date)

    @staticmethod
    def get_timestamp(days=0):
        '''
        获取timestamp
        :param days: n天前
        :return:n天前的timestamp(单位: ms)
        '''
        return int(time.time() * 1000 + days * 24 * 60 * 60 * 1000)

    @staticmethod
    def sleep(sleep_time):
        '''

        :param sleep_time: ms
        :return:
        '''
        time.sleep(sleep_time / 1000)

    @staticmethod
    def get_utc_time(format_date='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.utcnow().strftime(format_date)
