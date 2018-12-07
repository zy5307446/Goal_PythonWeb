#!/usr/bin/env python
# coding=utf-8

__metaclass__ = type

class K1():
    def fpp(self):
        print "K1-foo"
        
class K2():
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"
            
class J1(K2,K1):
    pass
        
class J2(K2,K1):
    def bar(self):
        print "J2-bar"
                
class C(J1,J2):
    pass

if __name__ == "__main__":
    print C.__mro__
    m = C()
    m.foo()
    m.bar()
