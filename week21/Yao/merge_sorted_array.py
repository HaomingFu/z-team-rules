#!/usr/bin/env python
# encoding: utf-8

#Status: Accepted
#From: https://oj.leetcode.com/problems/merge-sorted-array/
#Date: August 31

class Solution:
    # @param A a list of integers
    # @param m an integer, length of A
    # @param B, a list of integers
    # @param n, an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        ix = m + n -1
        ixa = m - 1
        ixb = n - 1
        while ixa >= 0 and ixb >= 0:
            if A[ixa] >= B[ixb]:
                A[ix] = A[ixa]
                ixa = ixa - 1
            else:
                A[ix] = B[ixb]
                ixb = ixb -1
            ix = ix - 1
        while ixb >= 0:
            A[ix] = B[ixb]
            ix = ix - 1
            ixb = ixb - 1
