#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/excel-sheet-column-number/

def titleToNumber(s):
    s = s.lower()
    colNum = 0
    for aChar in s:
        colNum = colNum * 26 + ord(aChar) - ord('a') + 1

    return colNum
