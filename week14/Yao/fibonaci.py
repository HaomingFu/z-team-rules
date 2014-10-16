#!/usr/bin/env python
# encoding: utf-8

a = 1
b = 2
sum = 0
while b < 4000000:
    b, a = a+b, b
    if a % 2 == 0:
        sum = sum + a

print(sum)
