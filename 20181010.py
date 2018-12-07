#!/usr/bin/env python
# coding:utf-8

all_user = ["python","go","Objective-C","Java","C#","C++"]

if "python" in all_user:
    all_user.remove("python")
    all_user.pop()
    all_user.reverse()
    print all_user
else:
    print "\"python\" is not in all_user"


