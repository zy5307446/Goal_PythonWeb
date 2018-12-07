#!/usr/bin/env python
# coding:utf-8

'''
# OOP三大特性：封装 继承 多态
# 今天讲讲继承：子类继承父类所有属性和方法；子类可新增、重新定义属性或重写方法
# 重度继承易臃肿，提倡基于接口类（几乎没代码）的轻度继承
# 子类方法和父类方法重名：重写，执行子类的方法
# 父类被重写覆盖的方法调用：super(子类，self).方法名
# 多重继承：class HotGirl(Person,Girl)
# 多重继承执行顺序：广度优先
# 通过实例调用父类方法，称为：方法绑定在实例上
# 非绑定方法：super调用
# 静态方法/类方法：直接用类.方法调用；也可实例调用即绑定实例调用

'''
__metaclass__ = type

class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print "i love you."

    def setHeigh(self):
        print "The heigh is: 1.60m."

    def breast(self,n):
        print "my breast is: .",n

class Girl(Person):
    def setHeigh(self):
        print "The heigh is: 1.70m."

if __name__ == "__main__":
    cang = Girl("canglaoshi")
    cang.setHeigh()
    cang.speak()
    cang.breast(90)



        
