#coding=utf-8
import os, pickle

# 用户类
class User:
    def __init__(self, name, uid, card):
        self.name = name
        self.uid = uid
        self.card = card

    def __str__(self):
        return '姓名:{} 身份证号:{} 银行卡:{}'.format(self.name, self.uid, self.card.cid)

    @staticmethod
    def save_info(userinfo):
        pathname = os.path.join(os.getcwd(), 'user_info.db')
        with open(pathname, 'wb') as fp:
            pickle.dump(userinfo, fp)

    @staticmethod
    def load_info():
        pathname = os.path.join(os.getcwd(), 'user_info.db')
        if os.path.exists(pathname):
            with open(pathname, 'rb') as fp:
                ret = pickle.load(fp)
                return ret
        else:
            return {}

