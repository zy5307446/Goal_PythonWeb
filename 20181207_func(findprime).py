#!/usr/bin/env python
# coding=utf-8
"""find primes"""
import math
def isprime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n/i == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [i for i in range(2,100) if isprime(i)]
    print primes
