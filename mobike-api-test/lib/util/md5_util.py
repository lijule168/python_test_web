#!/usr/bin/python
import hashlib
import base64,datetime

class MD5Util(object):
    str_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    def __init__(self):
        pass

    @staticmethod
    def abc(str):
        md5_str = hashlib.md5(str).digest()
        #print md5_str
        binpwd = [bin(int(i.encode('hex'), 16))[2:] for i in md5_str]
        intpwd = [MD5Util.bin2int(i) for i in binpwd]
        return intpwd

    @staticmethod
    def bin2int(bin):
        x = int(bin, 2)
        if len(bin) == 8:
            x -= 2 ** 8
        return x

    @staticmethod
    def get_md5_code(str):
        md5_str = MD5Util.abc(str)
        ret = ""
        for char in md5_str:
            #print char
            i_ret = char
            if i_ret< 0:
                i_ret = i_ret + 256
            id1 = i_ret / 16
            id2 = i_ret % 16

            ret = ret + MD5Util.str_digits[id1] + MD5Util.str_digits[id2]

        return ret

    # @staticmethod
    # def get_md5(str):
    #     md2 = hashlib.md5()
    #     md2.update(str)
    #     return md2.hexdigest()

    @classmethod
    def get_eption(cls, time_stamp, nu, if_epdata=1):
        if not isinstance(time_stamp, str):
            time_stamp = str(time_stamp)
        if not isinstance(nu, str):
            nu = str(nu)
        m = hashlib.md5()
        m.update((nu + '#' + time_stamp).encode(encoding="utf-8"))
        psw = m.hexdigest()
        if if_epdata:
            return psw[2:10]
        else:
            return psw[2:7]

    @classmethod
    def get_md5(cls, str_list):
        m = hashlib.md5()
        m.update(str_list.encode(encoding='utf-8'))
        md = m.hexdigest()
        return md

    @classmethod
    def get_sha1_encrypt(self,origin_str):
        """
        使用sha1加密算法，返回str加密后的字符串
        """
        sha = hashlib.sha1(origin_str.encode("utf-8"))
        encrypts = sha.hexdigest()
        return encrypts