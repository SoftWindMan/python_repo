#coding=utf-8
import hashlib
from random import randint

# help模块用于对卡号密码的创建
class Helper:
    # 生成银行卡号
    @staticmethod
    def generate_card_cid(length=8):
        cid = ''
        for i in range(length):
            cid += str(randint(0, 9))
        return cid

    # 加密用户密码信息
    @staticmethod
    def encry_pwd(pwd):
        m = hashlib.md5()
        m.update(pwd.encode('utf-8'))
        return m.hexdigest()

    # 核对用户信息
    @staticmethod
    def check_pwd(pwd, pwd_hash):
        m = hashlib.md5()
        m.update(pwd.encode('utf-8'))
        return m.hexdigest() == pwd_hash

