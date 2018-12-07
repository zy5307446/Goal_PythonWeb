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
        self.name = "qiwsir"
        self.__name = "kivi"
        
    @property
    def __python(self):
        print "I Love Cong."

    def code(self):
        print "Which language do you like?"
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    #p.code()
    #p.__python()
    #print p.me
    print p.__name
