#coding=utf-8

# 管理员类
class Admin:
    def __init__(self, name='admin', password='123456'):
        self.name = name
        self.password = password

    def welcome(self):
        print('欢迎使用xx银行系统')

    def login(self):
        name = input('请输入你的用户名：')
        password = input('请输入你的密码：')
        if name == self.name and password == self.password:
            return True
        else:
            return False

    def menu(self):
        print('建户【0】 销户【1】 查看余额【2】 存款【3】 取款【4】')
        print('转账【5】 锁卡【6】 解锁【7】 用户信息【8】 退出【9】')

