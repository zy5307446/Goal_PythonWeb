#!/usr/bin/env python
# coding:utf-8

'''
NameSpace：定义的命名和对象的映射集合
Local NameSpace -> Global NameSpace -> Built-in NameSpace
print locals()
print Globals()
作用域：程序直接可访问的命名空间


'''
def outer_foo():
    #global a #申明为全局变量
    a = 10
    def inner_foo():
        a = 20
        print "inner_foo, a=",a #a = 20

    inner_foo()
    print "outer_foo, a=",a #a =10

a = 30
outer_foo()
print "a=",a
