#!/usr/bin/python
# -*- encoding:utf-8 -*-

import os, logging, logging.config

from lib.util.path_util import config_path, proj_path

class Logger(object):
    """docstring for Logger"""
    __log = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger,cls).__new__(cls, *args, **kwargs)
            cls.__log = cls.__instance.initialLog("root")
        return cls.__instance

    def initialLog(self, moduleName="root"):
        if self.__log == None:
            self.create_dir(proj_path + "log")
            self.create_dir(proj_path + "report")
            configPath = config_path + "/log_conf.ini"
            logging.config.fileConfig(configPath)
            self.__log = logging.getLogger(moduleName)
        return self.__log

    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    @property
    def log(self):
        return self.__log

l = Logger().log