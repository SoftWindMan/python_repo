#coding=utf-8
from keepAccount.test.bank.help import Helper
from keepAccount.test.bank.user import User
from keepAccount.test.bank.card import Card

class Operate:
    def __init__(self, userinfo={}):
        self.userinfo = userinfo

    def new_user(self):
        name = input('请输入你的姓名：')
        uid = input('请输入你的身份证号：')
        pwd = input('请输入你的银行卡密码：')

        # 生成银行卡号和加密银行卡密码
        cid = Helper.generate_card_cid()
        pwd = Helper.encry_pwd(pwd)

        # 创建银行卡和用户对象
        card = Card(cid, pwd)
        user = User(name, uid, card)
        self.userinfo[cid] = user

        # 保存用户信息
        User.save_info(self.userinfo)
        print('开户成功！')

    def del_user(self):
        cid = input('请输入你的银行卡号：')
        if cid:
            user = self.userinfo[cid]
            count = 0
            while True:
                pwd = input('请输入你的银行卡密码：')
                if Helper.check_pwd(pwd, user.card.pwd):
                    del self.userinfo[cid]
                    User.save_info(self.userinfo)
                    print('销户成功！')
                    break
                else:
                    print('密码错误，请重新输入！')
                    count += 1
                    if count >= 3:
                        print('密码错误次数已达上限！')
        else:
            print('银行卡号不存在，请重新输入！')

    def query_money(self):
        cid = input('请输入你的银行卡号：')
        user = self.userinfo[cid]
        print('金融:{}'.format(user.card.money))

    def save_money(self):
        cid = input('请输入你的银行卡号：')
        user = self.userinfo[cid]
        count = 0
        if user.card.islock:
            print('你的银行卡已冻结！')
            return

        while True:
            pwd = input('请输入你的银行卡密码：')
            if Helper.check_pwd(pwd, user.card.pwd):
                money = int(input('请输入你要存入的金额：'))
                user.card.money += money
                User.save_info(self.userinfo)
                print('存款成功！')
                break
            else:
                print('密码错误，请重新输入！')
                count += 1
                if count >= 3:
                    print('密码错误次数已达上限！')

    def get_money(self):
        cid = input('请输入你的银行卡号：')
        user = self.userinfo[cid]
        count = 0
        if user.card.islock:
            print('你的银行卡已冻结！')
            return

        while True:
            pwd = input('请输入你的银行卡密码：')
            if Helper.check_pwd(pwd, user.card.pwd):
                money = int(input('请输入你要获取的金额：'))
                if user.card.money >= money:
                    user.card.money -= money
                    User.save_info(self.userinfo)
                    print('取款成功！')
                    break
                else:
                    print('余额不足！')
            else:
                print('密码错误，请重新输入！')
                count += 1
                if count >= 3:
                    print('密码错误次数已达上限，银行卡已锁定！')
                    user.card.islock = True

    def give_money(self):
        cid = input('请输入你的银行卡号：')
        user = self.userinfo[cid]
        count = 0
        if user.card.islock:
            print('你的银行卡已冻结！')
            return

        while True:
            pwd = input('请输入你的银行卡密码：')
            if Helper.check_pwd(pwd, user.card.pwd):
                cid1 = input('请输入你要转账的银行卡号：')
                user1 = self.userinfo[cid1]
                money = int(input('请输入你要转账的金额：'))
                user.card.money -= money
                user1.card.money += money
                User.save_info(self.userinfo)
                print('转账成功！')
                break
            else:
                print('密码错误，请重新输入！')
                count += 1
                if count >= 3:
                    print('密码错误次数已达上限，银行卡已锁定！')
                    user.card.islock = True

    def lock_card(self):
        cid = input('请输入你要锁定的银行卡号：')
        uid = input('请出示你的身份证：')
        user = self.userinfo[cid]
        if user.uid == uid:
            user.card.islock = True
            print('锁卡成功！')
        else:
            print('身份证错误！')

    def nolock(self):
        cid = input('请输入你要解锁的银行卡号：')
        uid = input('请出示你的身份证：')
        user = self.userinfo[cid]
        if user.uid == uid:
            user.card.islock = False
            print('解锁成功！')
        else:
            print('身份证错误！')

    def show(self):
        for i in self.userinfo:
            print(self.userinfo[i])


