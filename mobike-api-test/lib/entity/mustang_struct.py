from enum import Enum, unique

@unique
class DataCenterCode(Enum):
    ZH = 0
    US = 1
    EU = 2

@unique
class RoamingStatus(Enum):
    TRANSFER_PROCESSING = 0
    TRANSFER_FINISHED = 1
    TRANSFER_FAIL = 2

@unique
class PersonRoamingStatus(Enum):
    unknow = 0
    local = 1
    ROAMING = 2
    LOCAL_BACK = 3
    ROAMING_FINISH = 4
