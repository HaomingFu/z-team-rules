#!/usr/bin/env python
# encoding: utf-8

"""
 Given a list of n numbers, and a sume. To decide if you can find some number
 from the list whose sum equals the given value.

"""
num = [1, 2, 3, 7, 9]
sum = 12

def dfs(i, val, n):
    if n ==i:
        return val==sum

    if dfs(i+1, val, n):
        return True

    if dfs(i+1, val+num[i], n):
        return True

    return False

def solve():
    return dfs(0, 0, 5)

print(solve())

