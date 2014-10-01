#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/rotate-image/
# State: AC
# Date: Sep.30, 2014

def rotate(matrix):
    n = len(matrix)
    res = []
    for ix in range(0, n):
        li = []
        for jx in range(0, n):
            li.append(matrix[jx][ix])
        li.reverse()
        res.append(li)
    return res
