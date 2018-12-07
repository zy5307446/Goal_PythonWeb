#!/usr/bin/env python
# coding:utf-8



'''
多态：传参允许不同类型的数据，数据的校验交由方法做


'''

__metaclass__ = type

class Animal:
    def __init__(self, name = ''):
        self.name = name

    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print "Meow!"

class Dog(Animal):
    def talk(self):
        print "woof!"



a = Animal("zzzzz")
a.talk()

c = Cat("Missy")
c.talk()


d = Dog("Rocky")
d.talk()
