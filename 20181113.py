#! /usr/bin/env python
# coding:utf-8


def fib(n):
    result = ['a', 'b']
    for i in range(n-2):
        result.append(result[-2]+'+'+result[-1])
    return result

if __name__ == "__main__":
    lst = fib(10)
    print lst
