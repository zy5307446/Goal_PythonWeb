#!/usr/bin/env/ python
# coding:utf-8

print "请输入任意一个整数数字："

number = int(raw_input())

if number == 10:
    print "您输入的数字是： %d" % number
    print "You are smart."
elif number > 10:
    print "您输入的数字是： %d" % number
    print "This number is more than 10."
elif number < 10:
    print "您输入的数字是： %d" % number
    print "This number is less than 10."
else:
    print "Are you a human?"

