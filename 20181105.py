Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = [1.2.4.5.7]
SyntaxError: invalid syntax
>>> l= [1,2,4,5,7]
>>> sum(i % 2 == 0 for i in l)
2
>>> for i in l:
	if(i % 2 == 0):
		print i

		
2
4
>>> 
========== RESTART: d:/Users/zhang.yib/Desktop/Python/2018-11-01.py ==========
请输入任意一个整数数字：
101
您输入的数字是： 101
This number is more than 10.
>>> 
========== RESTART: d:/Users/zhang.yib/Desktop/Python/2018-11-01.py ==========
请输入任意一个整数数字：
101

Traceback (most recent call last):
  File "d:/Users/zhang.yib/Desktop/Python/2018-11-01.py", line 12, in <module>
    print "您输入的数字是： %d" % number
TypeError: %d format: a number is required, not str
>>> 
========== RESTART: d:/Users/zhang.yib/Desktop/Python/2018-11-01.py ==========
请输入任意一个整数数字：
101
您输入的数字是： 101
This number is more than 10.
>>> 
========== RESTART: d:/Users/zhang.yib/Desktop/Python/2018-11-01.py ==========
请输入任意一个整数数字：
101
您输入的数字是： 101
This number is more than 10.
>>> 
