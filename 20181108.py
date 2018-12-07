#! /usr/bin/env python
# coding:utf-8


import random
number = random.randint(1,101)
guess = 0

while True:
    number_input = raw_input("Please input the number you wanna: ")
    guess += 1
    if not number_input.isdigit():
        print "You cannt do this, you must input interger"
    elif int(number_input) < 0 or int(number_input) >= 100:
        print "You cannt do this, you must input an interger between 1 and 100"
    else:
        if number == int(number_input):
            print "OK, you are good, it's just %d that you  input"% number
            break
        elif number > int(number_input) or number < int(number_input):
            print "Sorry, you are wrong, please try again"
        else:
            print "Hold on, im sick, i need a rest"
