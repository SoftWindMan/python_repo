#coding=utf-8
from keepAccount.test.bank.admin import Admin
from keepAccount.test.bank.operate import Operate
from keepAccount.test.bank.user import User

# 创建管理员对象
admin = Admin()
admin.welcome()
count = 0

while True:
    ret = admin.login()

    # 加载用户信息
    userinfo = User.load_info()
    operate = Operate(userinfo)
    if ret:
        print('登录成功！')
        while True:
            admin.menu()
            num = int(input('请输入你要进行的操作：'))
            isbreak = False
            if num == 0:
                operate.new_user()
            if num == 1:
                operate.del_user()
            if num == 2:
                operate.query_money()
            if num == 3:
                operate.save_money()
            if num == 4:
                operate.get_money()
            if num == 5:
                operate.give_money()
            if num == 6:
                operate.lock_card()
            if num == 7:
                operate.nolock()
            if num == 8:
                operate.show()
            if num == 9:
                isbreak = True
                break

        if isbreak == True:
            break
    else:
        print('密码错误，请重新输入！')
        count += 1
        if count >=3:
            print('密码错误已达上限！')


