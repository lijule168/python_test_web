#!/usr/bin/python
# -*- coding:utf-8 -*-

class MBKImsiMobileRef:
    imsi_code = None
    mobile = None
    ts = None
    sys_user_id = None
    update_time = None
    telecoms = None
    select_column = "IMSI_CODE,MOBILE,TS,SYS_USER_ID,UPDATE_TIME,TELECOMS"

class MBKBikeHardware:
    bike_id = None
    rom_software_version = None
    imei = None
    imsi = None
    msisdn = None
    create_time = None
    lock_model = None
    bike_model = None
    ts = None
    hardware_version = None
    is_delete = None
    model_type = None
    register_time = None
    mac_addr = None
    bluetooth_app_version = None
    bluetooth_sd_version = None
    bluetooth_boot_version = None
    random_key = None
    telecoms = None
    registry_check_str = None
    select_column = "BIKE_ID,ROM_SOFTWARE_VERSION,IMEI,IMSI,MSISDN,CREATE_TIME,LOCK_MODEL,BIKE_MODEL,TS,HARDWARE_VERSION,IS_DELETE,MODEL_TYPE,REGISTER_TIME,MAC_ADDR,BLUETOOTH_APP_VERSION,BLUETOOTH_SD_VERSION,BLUETOOTH_BOOT_VERSION,RANDOM_KEY,TELECOMS,REGISTRY_CHECK_STR"