#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/majority-element/
# Date: Jan. 11, 2015

def majorityElement(num):
    map = {}

    for aValue in num:
        map[aValue]  = 1 if aValue not in map else map[aValue] + 1

    for each in map:
        if map[each] >= len(num) // 2:
            return each
    return None


aList = [1, 2, 3, 1, 1, 5, 6, 1, 1, 1]
print(majorityElement(aList))
