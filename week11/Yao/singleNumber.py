# From: https://oj.leetcode.com/problems/single-number/
# Date: May 22, 2014
# status: Accepted
# Given an array of integers, every elements appeares twice except for one. Find that
# single number in linear time without using extra memeory
class Solution:
    # @param A, a list
    # @return an integer
    def singleNumber(self, A):
        res = A[0]
        for i in A[1:len(A)]:
            res ^= i
        return i
