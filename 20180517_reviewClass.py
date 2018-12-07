#! /usr/bin/env python
#coding:utf-8
'''
# 类：熟悉+方法
# 实例：类的具体化
# 实例.属性；实例.方法
# __class__:查看对象类型
# type():也可查看对象类型
# 类定义：
# 1、class classname(object):
        program

  2、__metaclasee__ = type
    class classname:
        program
# 初始化函数：__init__
# self：接收实例化过程中传入的所有数据；实例与self对应，实例主外，self主内
# class/object.attribute：实现对属性的修改和增加
# 不可变对象：类属性不为实例属性改变而改变;实例属性受类属性改变而改变
# 可变对象：类属性与实例属性互相影响
# return：把数据从类里面传到类外面

'''
__metaclass__ = type 

class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def color(self,color):
        print "%s is %s" % (self.name,color)
