#!/usr/bin/python
# -*-coding=utf-8 -*-
from enum import Enum

__author__ = "dingbaixia@mobike.com"


class DynamicKeyParamEnum(Enum):
    USER_ID = "#user_id#"

class RedisKeyUtil(object):
    '''
    环境使用的redis key, 来源于开发,缺失的会后续增加
    '''
    #***********  订单数据库拆分的路由 ****************#
    DB_ORDER_ROUTE = "STRING_DB_ORDER_ROUTE"

    LIST_EMAIL_KEY = "LIST_EMAIL_KEY"
    LIST_MESSAGE_KEY = "LIST_MESSAGE_KEY"
    HASH_CONSRDS_KEY = "HASH_CONSRDS_KEY"
    HASH_USER_INFO = "HASH_USER_INFO"
    HASH_USER_SRAKEY = "HASH_USER_SRAKEY"

    HASH_BIKE_CORE_INFO = "HASH_BIKE_CORE_INFO"
    HASH_BIKE_OTA = "HASH_BIKE_OTA"
    HASH_BIKE_OTA_IDS = "HASH_BIKE_OTA_IDS"
    HASH_BIKE_OTA_FILE = "HASH_BIKE_OTA_FILE"
    HASH_BIKE_OTA_FILE_VESRION = "HASH_BIKE_OTA_FILE_VESRION"
    HASH_BIKE_OTA_CMD = "HASH_BIKE_OTA_CMD"
    HASH_BIKE_OTA_UPDATA = "HASH_BIKE_OTA_UPDATA"
    HASH_USER_TOKEN = "HASH_USER_TOKEN"
    HASH_BIKE_PACKET_TIMESTAMP = "HASH_BIKE_PACKET_TIMESTAMP"
    HASH_BIKE_PACKET_SERIALNUMBER = "HASH_BIKE_PACKET_SERIALNUMBER"
    HASH_BIKE_PACKET_SERIALNUMBER_CLIENT = "HASH_BIKE_PACKET_SERIALNUMBER_CLIENT"
    HASH_BIKE_LAST_LOCATION_TIME = "HASH_BIKE_LAST_LOCATION_TIME"
    HASH_BIKE_PACKET_STATUS = "HASH_BIKE_PACKET_STATUS"
    HASH_BIKE_PACKET_STATUS_FOR_MOCK_BIKE = "HASH_BIKE_PACKET_STATUS_FOR_MOCK_BIKE"
    HASH_BIKE_PACKET_STATISTICS = "HASH_BIKE_PACKET_STATISTICS"
    HASH_BIKE_PACKET_STATISTICS_FOR_MOCK_BIKE = "HASH_BIKE_PACKET_STATISTICS_FOR_MOCK_BIKE"
    HASH_BIKE_PACKET_PRECISELY_STATISTICS = "HASH_BIKE_PACKET_PRECISELY_STATISTICS"
    HASH_BIKE_AND_MPL_REFERENCE = "HASH_BIKE_AND_MPL_REFERENCE"
    HASH_MPL_AND_BIKES_REF_PREFIX = "HASH_MPL_AND_BIKES_REF_PREFIX_"

    HASH_ORDER_INFO = "HASH_ORDER_INFO"
    ##
    HASH_BIKE_LAST_TOW_LAG = "HASH_BIKE_LAST_TOW_LAG"
    HASH_USER_LONG = "HASH_USER_LONG"
    HASH_RUFUND_INFO = "HASH_RUFUND_INFO"
    HASH_FAULTS_INFO = "HASH_FAULTS_INFO"
    HASH_SHORT_URL = "HASH_SHORT_URL"
    HASH_OPERAREA_INFO = "HASH_OPERAREA_INFO"
    HASH_US_INFO = "HASH_US_INFO"
    HASH_US_USERID = "HASH_US_USERID"
    HASH_US_ID_INFO = "HASH_US_ID_INFO"

    HASH_MBKAPICONFIG_INFO = "HASH_MBKAPICONFIG_INFO"
    HASH_WHITE_USER_INFO="HASH_WHITE_USER_INFO"

    HASH_USER_REFINFO = "HASH_USER_REFINFO"

    HASH_INVITATION = "HASH_INVITATION_E"

    HASH_PRESENT = "HASH_PRESENT"

    HASH_SCHEDULE = "HASH_SCHEDULE"

    HASH_UPGRADE = "HASH_UPGRADE"
    ##
    HASH_TYPE_DISCOUNT = "HASH_TYPE_DISCOUNT"

    HASH_BIKE_PACKET_SESSION = "HASH_BIKE_PACKET_SESSION"

    HASH_SESSION_AND_BIKEID = "HASH_SESSION_AND_BIKEID"

    STRING_USEDID = "STRING_USEDID"

    STRING_SCHUEDULE_NUM = "STRING_SCHUEDULE_NUM"

    STRING_SCHUE_USER = "STRING_SCHUE_USER"

    #**用户预约蜂鸣总数**#
    STRING_USER_SCHUEDULE_BEEP_NUM = "STRING_USER_SCHUEDULE_BEEP_NUM"

    #**用户预约单车蜂鸣总数**#
    STRING_USER_SCHUEDULE_BIKE_BEEP_NUM = "STRING_USER_SCHUEDULE_BIKE_BEEP_NUM"

    MESSAGE_SHORT_LIST = "MESSAGE_SHORT_LIST"

    HASH_EMPLOYEE_INFO = "HASH_EMPLOYEE_INFO"
    STRING_EMPLOYEEID = "STRING_EMPLOYEEID"
    HASH_BIKE_WHITELIST = "HASH_BIKE_WHITELIST"
    HASH_OPERAT_AREA = "HASH_OPERAT_AREA"
    HASH_GEO_INFO = "HASH_GEO_INFO"
    HASH_API_ICON = "HASH_API_ICON"

    ##MESSAGE_SHORT_LIST HASH_EMPLOYEE_INFO HASH_OPERAT_MSG  HASH_GEO_INFO HASH_CONFIG_GEO HASH_CONFIG_SEARCH HASH_CONFIG_DEPOSIT HASH_CONFIG_UNLOCK
    HASH_OPERAT_MSG = "HASH_OPERAT_MSG"
    #**地理围栏**#
    HASH_CONFIG_GEO = "HASH_CONFIG_GEO"
    #**搜索半径配置**#
    HASH_CONFIG_SEARCH = "HASH_CONFIG_SEARCH"
    #**押金配置**#
    HASH_CONFIG_DEPOSIT = "HASH_CONFIG_DEPOSIT"
    #**开锁时间次数限制**#
    HASH_CONFIG_UNLOCK = "HASH_CONFIG_UNLOCK"
    #**预约**#
    HASH_BIKE_SCHEDU = "HASH_BIKE_SCHEDU"
    #**预约**#
    HASH_BIKE_SCHEDU_OBJECT = "HASH_BIKE_SCHEDU_OBJECT"

    #**用户预约蜂鸣**#
    HASH_USER_SCHEDU_BEEP = "HASH_USER_SCHEDU_BEEP"

    #**预约 开锁距离**#
    HASH_BIKE_UNLOCK_DIS = "HASH_BIKE_UNLOCK_DIS"
    CID = "HASH_APP_CID"

    HASH_BIKE_STOP_IMG = "HASH_BIKE_STOP_IMG"

    #**搜索半径配置**#
    HASH_CONFIG_SYSWH = "HASH_CONFIG_SYSWH"
    #*********app*用户信息****#
    HASH_USER_MSG = "HASH_USER_MSG"
    #*********app*用户信息读取****#
    HASH_USER_MSG_ISREAD = "HASH_USER_MSG_ISREAD"
    #*********app*用户信用值***#
    HASH_USER_CRI = "HASH_USER_CRI"

    #*********app*用户信用值***#
    HASH_USER_CRI_PM = "HASH_USER_CRI_PM"
    #*********app*用户信用值***#
    HASH_USER_PAY = "HASH_USER_PAY"

    #*********app*用户常用地址***#
    HASH_USER_ADDESS = "HASH_USER_ADDESS"
    #*********app*用户超时次数***#
    HASH_USER_ULOCK_TIMEOUT = "HASH_USER_ULOCK_TIMEOUT"

    #*********app*用户余额***#
    HASH_USER_VBALANCE = "HASH_USER_VBALANCE"
    #*********app*用户订单***#
    HASH_ORDER = "HASH_ORDER"
    #*********app*用户订单***#
    HASH_USERORDER = "HASH_USERORDER"

    HASH_OPS_SCHOOL = "HASH_OPS_SCHOOL_NWN"

    ORDER_TO_REGEO = "ORDER_TO_REGEO"
    #*********appconfiversion***#
    HASH_CONGING_VERSION = "HASH_CONGING_VERSION"
    #*********app*支付,身份证验证开关***#
    HASH_PAYOFON = "HASH_PAYOFON"
    #*********亿美接口***#
    HASH_IDTOKEN = "HASH_IDTOKEN"
    #*********自行车最后的经纬度新***#
    HASH_BIKE_LAST_LAG = "HASH_BIKE_LAST_LAG"
    #*********自行车骑行记录***#
    HASH_BIKE_RIDING_STRART = "HASH_BIKE_RIDING_STRART"
    HASH_DEPOST_PROB = "HASH_DEPOST_PROB"
    #*********自行车类型配置***#
    HASH_OPEA_CONFIG = "HASH_OPEA_CONFIG"
    #*********自行车类型配置***#
    HASH_OPEA_CITY_CONFIG = "HASH_OPEA_CITY_CONFIG"

    #*********红包车配置***#
    HASH_OPEA_REDPACKET_CONFIG = "HASH_OPEA_REDPACKET_CONFIG"

    HASH_OPEA_CONFIG_MOBLIE = "HASH_OPEA_CONFIG_MOBLIE"
    HASH_OPEA_TYPE = "HASH_OPEA_TYPE"
    #*********优惠券list***#
    HASH_USER_CP_LIST = "HASH_USER_CP_LIST"
    #*********优惠券信息***#
    HASH_CP_INFO= "HASH_CP_INFO"

    #*********优惠券信息***#
    HASH_CP_CFIG= "HASH_CP_CFIG"
    #*********优惠券发放配置***#
    HASH_CP_SEND_CF= "HASH_CP_SEND_CF"
    #*********兑换#活动发放配置***#
    HASH_DHHD_SEND_CF= "HASH_DHHD_SEND_CF"
    #*********保存所有已经被使用的优惠券ID**************#
    SET_ALL_COUPON_IDS = "SET_ALL_COUPON_IDS"
    #*********保存用户已经领取过的优惠券****************#
    LIST_USER_COUPON_SEND = "LIST_USER_COUPON_SEND"
    #*********兑换#活动发放配置***#
    HASH_RIDING_COUNT= "HASH_RIDING_COUNT"
    #*********累计骑行多少设置***#
    HASH_RIDING_COUNT_NUBER= "HASH_RIDING_COUNT_NUBER"
    #*********客服开关***#
    STRING_IMIN_KF= "STRING_IMIN_KF"
    #*********优惠券开关***#
    STRING_COUPON_KF= "STRING_COUPON_KF"
    #**************#
    LIST_COUPON_NUMBER_LOCK = "LIST_COUPON_NUMBER_LOCK"

    #***********用户负面记录*************#
    HASH_NEGATIVE_CREDIT = "HASH_NEGATIVE_CREDIT"

    #***********用户信用分*************#
    USER_CREDIT_VAL2  = "USER_CREDIT_VAL2_%s"
    #***********订单是否可以被更新************#
    HASH_ORDERS_UPDATE_LOCK = "HASH_ORDERS_UPDATE_LOCK_%s"
    #***********订单号是否可以被下发************#
    STRING_ORID_SEND = "STRING_ORID_SEND"
    #***********城市映射************#
    HASH_CITY_MAP = "HASH_CITY_MAP"
    #***********红包车每日设置信息************#
    HASH_REDPACKAGE_DATE_CONFIG = "HASH_REDPACKAGE_DATE_CONFIG"
    #***********自行车最后一次上报时间和当前时间的差值************#
    STRING_REPORT_LAST_TIME = "STRING_REPORT_LAST_TIME"
    #*********** 红包车free 时间 最后一次上报时间 ************#
    HASH_REDPACKAGE_CONFIG = "HASH_REDPACKAGE_CONFIG"
    #*********** 红包车红包列表缓存第一页***********************#
    HASH_REDPACKET_1ST_PAGE = "HASH_REDPACKET_1ST_PAGE"
    #************* 红包车用户提现错误次数 ******************#
    LIST_ERR_WITHDRAW_TIMES = "LIST_ERR_WITHDRAW_TIMES"

    #***********押金&车费重返配置************#
    HASH_PAY_RECHARGE_CONFIG = "HASH_PAY_RECHARGE_CONFIG"

    #***********banner配置************#
    HASH_BANNER_STRATEGY_CONFIG = "HASH_BANNER_STRATEGY_CONFIG"

    #***********banner缓存 主key***********#
    HASH_BANNER_STRATEGY_BESTMATCH_KEY = "HASH_BANNER_STRATEGY_BESTMATCH_KEY"


    #***********红包车用户每日提现次数*******************#
    HASH_RP_USER_WD_TIMES = "HASH_RP_USER_WD_TIMES"
    #***********红包车用户规则****************#
    HASH_REDBIKRE_USER = "HASH_REDBIKRE_USER"
    #*****查询条件映射 :根据用户城市编号获取需要查询的城市编号***#
    HASH_CITY_SELECT_MAP = "HASH_CITY_SELECT_MAP"

    #***********雅典娜的用户****************#
    HASH_ATHENA_USER = "HASH_ATHENA_USER"
    HASH_ATHENA_USER_LIST = "HASH_ATHENA_USER_LIST"

    #***********Bike ID to City Code mapping****************#
    HASH_BIKE_TO_CITY = "HASH_BIKE_TO_CITY"

    #***********did user get withdraw coupon****************#
    HASH_WD_COUPON = "HASH_WD_COUPON"

    #***********暗宝箱白名单文件****************#
    HASH_PRECIOUS_PHONE = "HASH_PRECIOUS_PHONE"

    #***********   彩蛋车 ****************#
    HASH_ACTIVITY_AWARD_KEY = "HASH_ACTIVITY_AWARD_KEY"

    #***********Auto end trip config****************#
    AUTO_END_TRIP_CONFIG = "AUTO_END_TRIP_CONFIG"
    AUTO_END_TRIP_HISTORY = "AUTO_END_TRIP_HISTORY"

    #***********  mola 工单地图 ****************#
    MOLA_WORK_MAP_KEY = "STRING_MOLA_WORK_MAP_AREA"

    #***********Multi token****************#
    MULTI_TOKEN_KEY = "MULTI_TOKEN_" + DynamicKeyParamEnum.USER_ID.value

    ##用于过滤重复消息
    MPL_OPRENLOCK_FILTER_PREFIX = "MPL_OPRENLOCK_FILTER_"
    GET_OPEN_CITY_LIST = "GET_OPEN_CITY_LIST"

    #***********新支付开关****************#
    NEW_PAYMENT_OFF = "NEW_PAYMENT_OFF"

    #*********** 微信充值立减活动,领取风控用户ID ****************#

    USER_ID_FOR_WX_RECHARGE = "USER_ID_FOR_WX_RECHARGE"
    WX_RECHARGE_PACKET_ENABLED = "WX_RECHARGE_PACKET_ENABLED"
    WX_RECHARGE_PACKET_BATCH_USAGE = "WX_RECHARGE_PACKET_BATCH_USAGE"
    WX_RECHARGE_PACKET_BATCH_PROBABILITY = "WX_RECHARGE_PACKET_BATCH_PROBABILITY"
    WX_RECHARGE_PACKET_BATCH_MONEY = "WX_RECHARGE_PACKET_BATCH_MONEY"
    WX_RECHARGE_RECEIVE_RISK_CONTROL = "WX_RECHARGE_RECEIVE_RISK_CONTROL"
    WX_RECHARGE_PACKET = "WX_RECHARGE_PACKET"

    #*********** 用户三方扩展信息,三方ID ****************#
    THIRD_ID_FOR_EXTEND = "THIRD_ID_FOR_EXTEND"

    #*********** 微信充值立减活动,发放红包风控 ****************#
    WX_RECHARGE_GENERATE_RISK_CONTROL = "WX_RECHARGE_GENERATE_RISK_CONTROL"

    #*********** 微信充值立减活动,风控规则 ****************#
    WX_RECHARGE_RISK_CONTROL_RULE = "WX_RECHARGE_RISK_CONTROL_RULE"

    #***********锁状态 *********************#
    MOBIKE_LOCK_STATUS = "MOBIKE_LOCK_STATUS_"

    STRING_ADOPTION_MENU_TIMES="STRING_ADOPTION_MENU_TIMES"
    #*********** 免押金按城市配置 ******************#
    HASH_FREE_DEPOSIT_CONFIG = "HASH_FREE_DEPOSIT_CONFIG"
    #*********** 月卡配置 ***********#
    MONTH_CARD_CONFIG_N = "MONTH_CARD_CONFIG_N"
    #***********

    #***********用户红包免费骑行****************#
    HASH_RED_PACKET_FREE_CHARGE = "red_packet_free_charge_v1"

    #** ** ** ** ** 所有已开通产品 ** ** ** ** ** #
    FREE_DEPOSIT_PRODUCT_ALL = "FREE_DEPOSIT_PRODUCT_ALL"

    #用户详细信息缓存
    USER_INFO_USERID_V1 = "USER_INFO_USERID_V1_" + DynamicKeyParamEnum.USER_ID.value
