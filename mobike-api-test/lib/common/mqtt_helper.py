#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function

import random
import time
from threading import Thread

import paho.mqtt.client as mqtt

from lib.common.config_helper import EnvConfig
from lib.util.log_util import l


def on_connect(client, userdata, flags, rc):
    """连接回调（排查用
    """
    l.info("Connected with result code {}".format(rc))


def on_disconnect(client, userdata, rc):
    """断开连接回调（排查用）
    """
    l.info("Disconnected with result code {}".format(rc))


def wrap_on_message(buffer):
    """接收消息回调
    将收到的消息放到传入的 buffer 中
    异步回调转同步返回值
    """

    def on_message(client, userdata, msg):
        l.info("Received message with topic: {}, payload: {}".format(
            msg.topic, msg.payload))
        buffer.append(msg)

    return on_message


def on_subscribe(client, userdata, mid, granted_qos):
    """订阅回调（排查用）
    """
    l.info("Subscribed with granted qos {}".format(granted_qos))


def on_unsubscribe(client, userdata, mid):
    """取消订阅回调（排查用）
    """
    l.info("Unsubscribed with user data: {}".format(userdata))


def on_publish(client, userdata, mid):
    """发送回调（排查用）
    """
    l.info("Published with user data: {}".format(userdata))


class MQTTClient(object):
    """ MQTT Client
    将 mqtt 订阅信息的异步回调方式转变成了同步获取，方便测试收发消息的功能
    """

    def __init__(self, host=None, port=1883, client_id=None):
        self.port = port
        if host:
            self.host = host
        else:
            self.host = EnvConfig().mobike_mqtt_service.mqtt_host
        if client_id:
            self.client_id = client_id
        else:
            # 随机生成 internal 的 id，必须匿名登录，可以绕过鉴权
            self.client_id = "internal-testing-{}".format(
                random.randint(0, 10000))

    def connect(self, username=None, password=None):
        """连接 mqtt broker
        启动一个 daemon 线程接收消息
        """
        self.client = mqtt.Client(self.client_id, clean_session=False)
        if username:
            self.client.username_pw_set(username, password)
        self.client.on_connect = on_connect
        self.client.on_publish = on_publish
        self.client.on_subscribe = on_subscribe
        self.client.on_unsubscribe = on_unsubscribe
        self.client.on_disconnect = on_disconnect
        self.client.connect(self.host, self.port)
        # 使用 daemon 线程启动
        thread = Thread(target=self.client.loop_forever)
        thread.daemon = True
        thread.start()

    def subscribe(self, topic):
        """订阅消息
        返回一个订阅对象，该对象可以接收一段时间的消息并同步获取这些消息
        """
        return Subscription(self.client, topic)

    def publish(self, topic, payload):
        """发送消息
        """
        self.client.publish(topic, payload, qos=1)

    def disconnect(self):
        """断开连接
        断开连接会释放掉连接时开启的线程（因为 loop_forever 方法结束）
        """
        self.client.disconnect()


class Subscription(object):
    """订阅信息
    主要是为了同步获取一段时间内订阅的消息
    """

    def __init__(self, client, topic):
        self.client = client
        self.topic = topic
        self.msgs = []
        self.client.on_message = wrap_on_message(self.msgs)
        self.client.subscribe(self.topic)

    def get_msgs(self, timeout=10):
        """获取消息
        等待一段时间并获取所有消息
        """
        times = 0
        while times < timeout:
            time.sleep(1)
            times += 1
        self.client.unsubscribe(self.topic)
        return self.msgs

    def get_first_msg(self, timeout=10):
        """获取消息
        等待一段时间并获取第一条消息
        """
        times = 0
        while not self.msgs and times < timeout:
            time.sleep(1)
            times += 1
        self.client.unsubscribe(self.topic)
        if self.msgs:
            return self.msgs[0]
        return None
