#!/usr/bin/env python
# encoding: utf-8

# From:https://oj.leetcode.com/problems/valid-parentheses/
# Date: Oct. 2, 2014
# Status: AC

def isValid(s):
    stack = []
    for c in s:
        if c in ['(', '{',"]"]:
            stack.append(c)
        else:
            n = len(stack)
            if n == 0:
                return False
            tmp = stack.pop(n-1)
            if not (tmp,c) in [('(',')'), ('{','}'),('[',']')]:
                return False
    return len(stack)==0
