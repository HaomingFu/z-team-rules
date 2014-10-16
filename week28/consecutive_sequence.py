#!/usr/bin/env python
# encoding: utf-8

def longestConsecutive(num):
    num_set = set(num)
    m = 1

    for val in num:
        left = val -1
        right = val + 1
        count = 1


