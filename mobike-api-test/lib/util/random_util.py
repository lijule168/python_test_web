#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random, uuid, time,string


class RandomUtil(object):
    @classmethod
    def gen_phone_num(cls, prefix="138", phone_len=8):
        '''
        生成手机号
        :param prefix: 手机的前段
        :param phone_len: 随机生成数字的长度,用于手机的后段
        :return: 返回手机号
        '''
        phone_num = prefix + "".join(random.choice("0123456789") for i in range(phone_len))

        return str(phone_num)

    def get_unuse_phone_num(self):
        pass

    @classmethod
    def get_lock_id(cls):
        '''
        获取锁的id
        :return:
        '''
        lock_id = "".join(random.choice("0123456789") for i in range(10))
        return lock_id

    @classmethod
    def get_lag(cls):
        '''
        获取经纬度信息
        :return:
        '''
        longitude = random.uniform(-180, 180)
        latitude = random.uniform(-90, 90)
        return {"longitude": longitude, "latitude": latitude}

    @classmethod
    def get_order_id(cls):
        '''
        获取订单ID
        :return:
        '''
        order_id = "MBK" + "".join(random.choice("0123456789") for i in range(23))
        return order_id

    @classmethod
    def get_userid(cls):
        '''
        获取userid
        :return:
        '''
        return "".join(random.choice("123456789") for i in range(27))

    @classmethod
    def get_redpacket_id(self):
        '''
        获得红包ID
        :return:
        '''
        redpaket_id = 'RP'+''.join([random.choice(string.digits) for i in range(37)])
        return  redpaket_id


    @classmethod
    def get_uuid(cls):
        '''
        获取UUID
        :return:
        '''
        return str(uuid.uuid1())

    @classmethod
    def get_bikeid(cls):
        '''
        获取车的id
        :return:
        '''
        lock_id = int("".join(random.choice("123456789") for i in range(10)))
        return lock_id

    @classmethod
    def get_long(cls, num_len=8):
        return  int("".join(random.choice("123456789") for i in range(num_len)))

    @classmethod
    def get_hex_str(cls, num_len=16):
        """
        生成16进制字符串
        :param num_len:
        :return:
        """
        return ("".join(random.choice("123456789abcdef") for i in range(num_len)))