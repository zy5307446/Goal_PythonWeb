#! /usr/bin/env python
# coding:utf-8

def add_function(a,b):
    return a + b

def sub_function(c,d):
    return c - d

def mul_function(e,f):
    return e * f

def div_function(h,i):
    return h / i

if __name__ == "__main__":
    result = div_function(mul_function(add_function(2,3),sub_function(19,4)),3)
    print result
