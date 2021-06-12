#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class BannerReq(BaseReq):
    BANNER_GET_HOMEBANNERNATIVE = "api/v2/getHomeBannerNative.do"
    # 获取首页banner， 和user id相关， 无缓存， 性能比较差，目前在weixin中使用，
    BANNER_GETHOMEBANNER = "api/v2/getHomeBanner.do"

    # 添加banner-产品策略基本配置
    BANNER_ADD_BANNERSTRATEGY = "athena/banner/strategy/addBannerStrategy.do"

    # 删除数据库中的banner-产品策略基本配置
    BANNER_DELETE_BANNERSTRATEGY = "athena/banner/strategy/deleteBannerStrategy.do"

    # 删除cache指定的产品策略基本配置
    BANNER_DELETE_BANNERSTRATEGY_FROMCACHE = "athena/banner/strategy/deleteBannerStrategyFromCache.do"

    # 删除cache中所有的产品策略基本配置
    BANNER_DELETE_ALL_BANNERSTRATEGY_FROMCACHE = "athena/banner/strategy/deleteAll.do"
    # 根据cityCode获取Banner产品策略
    BANNER_QUERYBANNERSTRATEGY = "athena/banner/strategy/queryBannerStrategy.do"

    def __init__(self):
        super(BannerReq, self).__init__()

    def addBannerStrategy(self, param_dict, files):
        '''
        添加Banner strategy到数据库
        :param param_dict: 请求参数信息
        :return:
        '''

        return self.request("POST", self.BANNER_ADD_BANNERSTRATEGY, params=param_dict, files=files)

    def query_bannerstrategy(self, param_dict):
        '''
        根据cityCode获取Banner产品策略
        :param param_dict:
        :return:
        '''
        return self.request("GET", self.BANNER_QUERYBANNERSTRATEGY, params=param_dict)

    def del_bannerstrategy_in_db(self, param_dict):
        '''
        从数据库删除Banner strategy
        :param param_dict:
        @RequestParam(value = "bannerId", defaultValue = "", required = false) String bannerId,
                                         @RequestParam(value = "bannerCitycode", required = false) String bannerCitycode,
                                         @RequestParam(value = "bannerPriority", required = false) String bannerPriority,
                                         @RequestParam(value = "bannerText", required = false) String bannerText,
                                         @RequestParam(value = "bannerPicture", required = false) MultipartFile bannerPicture,
                                         @RequestParam(value = "bannerPictureThree", required = false) MultipartFile bannerPictureThree,
                                         @RequestParam(value = "bannerCategory", required = false) String bannerCategory,
                                         @RequestParam(value = "bannerContent", required = false) String bannerContent,
                                         @RequestParam(value = "isdelete", required = false) String isdelete,
                                         @RequestParam(value = "expireTime", required = false) String expireTime,
                                         @RequestParam(value = "ifUserid", required = false) String ifUserid)
        :return:
        '''
        return self.request("GET", self.BANNER_DELETE_BANNERSTRATEGY, params=param_dict)

    def del_bannerstrategy_with_citycode_from_cache(self, param_dict):
        '''
        从cache中删除特定城市的bannerstrategy
        :param param_dict: 城市的id dict
        :return:
        '''
        return self.request("GET", self.BANNER_DELETE_BANNERSTRATEGY_FROMCACHE, params=param_dict)

    def del_all_bannerstrategy_from_cache(self):
        '''
        从cache中删除所有bannerstrategy
        :return:
        '''
        return self.request("GET", self.BANNER_DELETE_ALL_BANNERSTRATEGY_FROMCACHE)

    def get_homebannernative(self, param_dict, header_dict):
        '''
        获取homebanner
        :param header_dict: 请求头信息
        :param param_dict: 请求参数信息
        :return:
        '''
        return  self.request("GET", self.BANNER_GET_HOMEBANNERNATIVE, params=param_dict, headers=header_dict)


    def get_homebanner(self, param_dict, header_dict):
        '''
        获取首页banner， 和user id相关， 无缓存， 性能比较差，目前在weixin中使用
        :param header_dict: 请求头信息
        :param param_dict: 请求参数信息
        :return:
        '''
        return  self.request("GET", self.BANNER_GETHOMEBANNER, params=param_dict, headers=header_dict)
