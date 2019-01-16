#coding=utf-8

# 银行卡类
class Card:
    def __init__(self, cid, pwd):
        self.cid = cid
        self.pwd = pwd
        self.money = 0
        self.islock = False

