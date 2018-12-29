#coding=utf-8

#一切皆文件
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()
yingpanwenjian=Sata()
jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)

class Alipay:
    '''
    支付宝支付
    '''
    def pay(self,money):
        print('支付宝支付了%s元'%money)

class Applepay:
    '''
    apple pay支付
    '''
    def pay(self,money):
        print('apple pay支付了%s元'%money)

class Wechatpay:
    def pay(self,money):
        '''
        实现了pay的功能，但是名字不一样
        '''
        print('微信支付了%s元'%money)

def pay(payment,money):
    '''
    支付函数，总体负责支付
    对应支付的对象和要支付的金额
    '''
    payment.pay(money)


p = Wechatpay()
pay(p,200)   #执行会报错
