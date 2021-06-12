"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""

__author__ = "dingbaixia@mobike.com"


class BaseEntity(object):
    def __init__(self):
        pass

    def to_object(self, obj):
        for key in dict(obj).keys():
            self.__setattr__(key, obj[key])
        return self


    def to_json(self):
        pass