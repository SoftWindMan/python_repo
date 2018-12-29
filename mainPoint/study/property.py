#coding=utf-8
import math
class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2 #计算面积

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius #计算周长

class Goods:

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

class A:
    __role = 'CHINA'
    @classmethod
    def show_role(cls):
        print(cls.__role)

    @staticmethod
    def get_role():
        return A.__role

    @property
    def role(self):
        return self.__role

a = A()
print(a.role)
print(a.get_role())
print(A.get_role())
a.show_role()
A.show_role()


