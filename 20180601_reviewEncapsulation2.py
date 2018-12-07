#! /usr/bin/env python
# coding:utf-8

'''
封装：Encapsulation
对对象的一种抽象，外部无法调用
__Attribute
__Method
访问私有属性可用@property置于方法之前声明

'''

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    @property
    def name(self):
        return self.__name

if __name__ ==  "__main__":
    p = ProtectMe()
    print p.name
