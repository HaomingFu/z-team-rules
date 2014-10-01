#!/usr/bin/env python
# encoding: utf-8

# Status: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Date: Sep.30, 2014
# Status: AC

def removeDuplicates( A):
    n = len(A)
    if n <= 2:
        return n
    ix = iter = 2
    while iter < n:
        if A[ix-2]!= A[iter]:
            A[ix] = A[iter]
            ix += 1
        iter += 1
    return ix


A= [1,1,1,2,3]
print(removeDuplicates(A))
print(A)
