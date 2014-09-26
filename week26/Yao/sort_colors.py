#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/sort-colors/
# Status: AC
# Date: Sep. 25

class Solution:
    def sortColors(self, A):
        blue = red = white = -1
        for i in A:
            if i==0:
                blue += 1
                white += 1
                red += 1
                A[blue], A[white], A[red] = 2, 1, 0
            if i == 1:
                blue += 1
                white += 1
                A[blue], A[white] = 2, 1
            if i == 2:
                blue += 1
                A[blue] = 2
