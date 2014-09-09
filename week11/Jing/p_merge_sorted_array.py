"""
From: http://oj.leetcode.com/problems/merge-sorted-array/
Author: Jing Zhou
Date: May 19, 2014
Thought: quite easy... but can be done in linear time... the key is do it backwards
"""



class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    def merge(self, A, m, B, n):
        i, j, k = m-1, n-1, m+n-1
        while k >= 0:
            if j < 0 or i >= 0 and A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A

    def merge(self, A, m, B, n):
        A[m:m+n] = B[0:n]
        return A.sort()
