#!/usr/bin/env python
# encoding: utf-8

def partition(s):
    if not s:
        return []
    if len(s)==1:
        return [[s]]
    res = []
    if isPalindrome(s):
        res.append([s])

    lists = partition(s[1:])
    res += [[s[0]]+li for li in lists]

    for ix in range(1, len(s)):
        if isPalindrome(s[:ix+1]):
            lists = partition(s[ix+1:])
            res += [[s[:ix+1]] +li for li in lists]

    return res

def isPalindrome(s):
    return s == s[::-1]


s = 'aabb'
print(partition(s))

